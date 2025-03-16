#Maintainer: Hitori-Laura <hitori_laura_sorgente@proton.me>
pkgname=weather-fetch
pkgver=1.0.0
pkgrel=1
pkgdesc="CLI app that fetches your position with geocoder and retrieves weather forecasts from the Open Meteo API"
arch=('any')
url="https://github.com/Hitori-Laura/weather-fetch"
license=('GPL3')
depends=('python' 'python-geocoder' 'python-requests', 'python-colorama')
makedepends=('python-setuptools')
source=("git+https://github.com/Hitori-Laura/weather-fetch.git")
sha256sums=('SKIP') # Using git source, so no need for sha256sum

# Prepare function to set up the environment
prepare() {
  cd "$srcdir/weather-fetch"
  # Ensure dependencies are listed in requirements.txt
}

# Build function to package the application
build() {
  cd "$srcdir/weather-fetch"
  python setup.py build
}

# Package function to install the package
package() {
  cd "$srcdir/weather-fetch"
  python setup.py install --root="$pkgdir/" --optimize=1
}
