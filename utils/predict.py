def predict(form_dict):
    import pickle
    with open("utils/Logistic_Regression.pkl", "rb") as f:
        model = pickle.load(f)
    print(model)
    return 0
