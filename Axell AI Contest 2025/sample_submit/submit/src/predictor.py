import cv2

class Predictor(object):
    @classmethod
    def get_model(cls, model_path):
        """Get model method

        Args:
            model_path (str): Path to the trained model directory.

        Returns:
            bool: The return value. True for success, False otherwise.
        """
        # load some model(s)
        cls.model = None
        return True

    @classmethod
    def predict(cls, input):
        """Predict method

        Args:
            input (str): path to the image you want to make inference from

        Returns:
            list[dict]: Inference for the given input.
        """
        # load an image and get the file name
        #img = cv2.imread(input)
        height, width, _ = input.shape
        
        predict_list = []
        predict_list.append({"category_id": 1, "bbox": [0, 0, width, height], "score": 1.0})
        return predict_list