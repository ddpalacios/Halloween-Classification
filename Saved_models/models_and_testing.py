from keras.models import load_model
import numpy as np
def load_models():
    model1 = load_model('Halloween_model_edition_80.h5')
    print("\nmodel1 loaded")
    model2 = load_model('Halloween_model_edition_73.h5')
    print("\nmodel2 loaded")
    model3 = load_model("Halloween_model_edition_78.h5")
    print("\nmodel3 loaded")

    return model1, model2,model3





model1,model2,model3 = load_models()


np.savez_compressed('halloween_models.npz',
                    model_80=model1,
                    model_73=model2,
                    model_78=model3)

