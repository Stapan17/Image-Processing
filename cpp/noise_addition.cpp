// This code snippet adds noise to RGB images
// Useful for image augmentation
void saltAndPepperNoise(Mat & image, const double noiseProbability)
{
	int imageChannels = image.channels();

        random_value_generator random; 

	long noisePoints = noiseProbability * image.rows * image.cols * imageChannels; // long var for decimal point calculation

	for (long i = 0; i < noisePoints; i++)
	{
		int row = random.get_integer(image.rows);

		int column = random.get_integer(image.cols);

		unsigned char newValue = random.get_boolean() ? 255 : 0; // RGB values lie b/w [0, 255]

		for (int channel = 0; channel < imageChannels; channel++)
		{
			unsigned char * pixelValuePtr = image.ptr(row) + (column * imageChannels) + channel;

			*pixelValuePtr = newValue; // Changes the pixels from intial RGB value to noise value
		}
	}
}
