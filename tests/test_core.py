from fractales.core import mandelbrot_escape_iterations, julia_escape_iterations,burning_ship_escape_iterations

def test_mandelbrot_zero_does_not_escape():
    result,b= mandelbrot_escape_iterations( 0 + 0j, 50)
    assert result ==50

def test_mandelbrot_two_escapes_quickly():
    result,b= mandelbrot_escape_iterations( 2 + 0j, 50)
    assert result <50

def test_mandelbrot_two_escapes():
    result,b = mandelbrot_escape_iterations( 1 + 0j, 25)
    assert 0 <= result <= 25

def test_julia_zero_does_not_escape():
    result,b= julia_escape_iterations( 0 + 0j,0j, 30)
    assert result ==30

def test_julia_two_escapes_quickly():
    result,b= julia_escape_iterations( 2 + 0j,0j, 30)
    assert result <50

def test_julia_two_escapes():
    result,b = julia_escape_iterations( 0.2 + 0.1j,-1.0+0.1j, 40)
    assert 0 <= result <= 40

def test_burning_ship_zero_does_not_escape():
    result,b= burning_ship_escape_iterations(0j,50)
    assert result ==50

def test_burning_ship_zero_does_escape():
    result,b= burning_ship_escape_iterations(2+0j,50)
    assert result <50