import pytest
import pygame
from unittest.mock import Mock, patch
from ship import Ship
from settings import Settings


@pytest.fixture
def mock_game():
    """Lightweight mock game object for testing"""
    game = Mock()
    game.settings = Settings()
    game.screen = Mock()
    game.screen.get_rect.return_value = pygame.Rect(0, 0, 800, 600)
    return game


@pytest.fixture
def ship(mock_game):
    """Create ship instance for testing"""
    with patch('pygame.image.load') as mock_load:
        mock_surface = Mock()
        mock_surface.get_rect.return_value = pygame.Rect(0, 0, 50, 50)
        mock_load.return_value = mock_surface
        
        ship = Ship(mock_game)
        ship.rect.center = (400, 300)  # Center position
        ship.x = float(ship.rect.x)
        ship.y = float(ship.rect.y)
        return ship


def test_current_ship_prevents_diagonal_movement(ship):
    """Test that current implementation prevents diagonal movement (demonstrates the bug)"""
    initial_x, initial_y = ship.x, ship.y
    
    # Try to move diagonally (right + up)
    ship.moving_right = True
    ship.moving_up = True
    ship.update()
    
    # Current implementation should only move in one direction due to elif
    moved_x = ship.x != initial_x
    moved_y = ship.y != initial_y
    
    # This test documents current broken behavior
    assert not (moved_x and moved_y), "Current implementation should prevent diagonal movement"


@pytest.mark.parametrize("right,left,up,down,expected_directions", [
    (True, False, True, False, 2),   # right + up = 2 directions
    (True, False, False, True, 2),  # right + down = 2 directions  
    (False, True, True, False, 2),  # left + up = 2 directions
    (False, True, False, True, 2),  # left + down = 2 directions
])
def test_ship_should_move_diagonally(ship, right, left, up, down, expected_directions):
    """Test desired behavior: ship should move diagonally when multiple keys pressed"""
    initial_x, initial_y = ship.x, ship.y
    
    # Set movement flags for diagonal movement
    ship.moving_right = right
    ship.moving_left = left  
    ship.moving_up = up
    ship.moving_down = down
    
    # This will be our target behavior after fixing the elif issue
    # For now, this test will fail with current implementation
    ship.update()
    
    # Count how many directions the ship actually moved
    directions_moved = 0
    if ship.x != initial_x:
        directions_moved += 1
    if ship.y != initial_y:
        directions_moved += 1
        
    assert directions_moved == expected_directions, f"Ship should move in {expected_directions} directions simultaneously"


def test_ship_movement_boundaries_during_diagonal(ship):
    """Test that diagonal movement respects screen boundaries"""
    # Position ship near top-right corner
    ship.rect.right = ship.screen_rect.right - 1
    ship.rect.top = 1
    ship.x = float(ship.rect.x)
    ship.y = float(ship.rect.y)
    
    # Try to move diagonally up-right (should be blocked)
    ship.moving_right = True
    ship.moving_up = True
    ship.update()
    
    # Should not move beyond boundaries
    assert ship.rect.right <= ship.screen_rect.right
    assert ship.rect.top >= 0


def test_single_direction_movement_still_works(ship):
    """Ensure single direction movement continues to work"""
    initial_x, initial_y = ship.x, ship.y
    
    # Test single direction movements
    test_cases = [
        ('moving_right', True, lambda: ship.x > initial_x),
        ('moving_left', True, lambda: ship.x < initial_x), 
        ('moving_up', True, lambda: ship.y < initial_y),
        ('moving_down', True, lambda: ship.y > initial_y),
    ]
    
    for attr, value, check_func in test_cases:
        # Reset position
        ship.rect.center = (400, 300)
        ship.x = float(ship.rect.x) 
        ship.y = float(ship.rect.y)
        
        # Reset all movement flags
        ship.moving_right = ship.moving_left = ship.moving_up = ship.moving_down = False
        
        # Set specific movement
        setattr(ship, attr, value)
        ship.update()
        
        assert check_func(), f"Single direction movement {attr} should work"