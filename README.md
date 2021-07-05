# Gaussian Blur Algorithm

A 2D implementation of the Gaussian Blur algorithm. This implementation processes pixel by pixel in 2 dimensions, making it quite slow. It could be sped up by using a property of the Gaussian function and process each pixel as the composition of 2 1D blurs. A simplistic solution to the edge cases is taken by returning the value for the current pixel if the offset value is out of bounds of the image.

### Reference resources
- https://www.pixelstech.net/article/1353768112-Gaussian-Blur-Algorithm
- https://en.wikipedia.org/wiki/Gaussian_blur
