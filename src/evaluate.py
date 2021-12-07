"""Evaluate the performance of the trained model."""
# from model import load_data
# from utils import load_model


def evaluate_model(model, test_images, test_labels):
    """Evaluate the model performance

    Args:
        model ([type]): fitted model
        test_images (np.ndarray): features for evaluation
        test_labels (np.ndarray): labels for evaluation
    """
    loss, acc, auc = model.evaluate(test_images, test_labels, verbose=2)
    print('Restored model, accuracy: {:5.2f}%'.format(100 * acc))
    print(model.predict(test_images))


# def main():
#     model = load_model()
#     print(type(model))
#     data_infile = "../data/protein_processed_data.pkl"
#     X_train, X_test, y_train, y_test = load_data(data_infile)
#     evaluate_model(model, X_test, y_test)


# if __name__ == "__main__":
#     main()
