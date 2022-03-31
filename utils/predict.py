def predict(form_dict):
    def warn(*args, **kwargs):
        pass
    import warnings
    warnings.warn = warn
    
    form_dict = preprocess(form_dict)
    # print(form_dict)

    import pickle
    model = pickle.load(open('utils/Logistic_Regression.pkl', 'rb'))

    p = model.predict([ list(form_dict.values()) ])
    
    return p

binary_cols = [
    'smoke',
    'alcohol',
    'stroke',
    'diffwalking',
    'diabetic',
    'exercise',
    'asthama',
    'kidney',
    'skincancer'
]

age_vals = [
    '18-24',
    '25-29',
    '30-34',
    '35-39',
    '40-44',
    '45-49',
    '50-54',
    '55-59',
    '60-64',
    '65-69',
    '70-74',
    '75-79',
    '80 or older'
]

race_vals = [
    'American Indian/Alaskan Native',
    'Asian',
    'Black',
    'Hispanic',
    'Other',
    'White'
]

health_vals = [
    'Poor', 
    'Fair', 
    'Good', 
    'Very good', 
    'Excellent'
]

def preprocess(form_dict):
    import pickle
    scalers = pickle.load(open('utils/scalers.pkl', 'rb'))
    # scalers = [
    #     age_scaler,
    #     health_scaler,
    #     bmi_scaler,
    #     physical_scaler,
    #     mental_scaler,
    #     sleep_scaler,
    # ]
    for key in form_dict.keys():
        if key in binary_cols:
            form_dict[key] = 1 if form_dict[key] == 'yes' else 0

        elif key == 'gender':
            form_dict[key] = 1 if form_dict[key] == 'Male' else 0

        elif key == 'age':
            form_dict[key] = age_vals.index(form_dict[key])
            form_dict[key] = scalers[0].transform([[ form_dict[key] ]])[0][0]

        elif key == 'race':
            form_dict[key] = race_vals.index(form_dict[key])
            race_dict = {}
            for i in range(6):
                race_dict[str(i)] = 0
                if i == form_dict[key]:
                    race_dict[str(i)] = 1

        elif key == 'health':
            form_dict[key] = health_vals.index(form_dict[key])
            form_dict[key] = scalers[1].transform([[ form_dict[key] ]])[0][0]
        elif key == 'bmi':
            form_dict[key] = scalers[2].transform([[ form_dict[key] ]])[0][0]

        elif key == 'physical':
            form_dict[key] = scalers[3].transform([[ form_dict[key] ]])[0][0]
        
        elif key == 'mental':
            form_dict[key] = scalers[4].transform([[ form_dict[key] ]])[0][0]
        elif key == 'sleep':
            form_dict[key] = scalers[5].transform([[ form_dict[key] ]])[0][0]

    form_dict.update(race_dict)
    del form_dict['race']

    return form_dict
