from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


MODEL_PATH = Path(__file__).parent / "models" / "iris_extra_trees_model.joblib"
FEATURES = {
    "Sepal length (cm)": "SepalLengthCm",
    "Sepal width (cm)": "SepalWidthCm",
    "Petal length (cm)": "PetalLengthCm",
    "Petal width (cm)": "PetalWidthCm",
}


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


def main() -> None:
    st.set_page_config(page_title="Iris Classifier", page_icon="🌸")
    st.title("Iris species classifier")
    st.write("Adjust the flower measurements to classify an Iris with the trained Extra Trees model.")

    with st.sidebar:
        st.header("Flower measurements")
        values = {
            column: st.slider(label, min_value=0.0, max_value=10.0, value=default, step=0.1)
            for label, (column, default) in {
                "Sepal length (cm)": ("SepalLengthCm", 5.1),
                "Sepal width (cm)": ("SepalWidthCm", 3.5),
                "Petal length (cm)": ("PetalLengthCm", 1.4),
                "Petal width (cm)": ("PetalWidthCm", 0.2),
            }.items()
        }

    try:
        model = load_model()
    except (FileNotFoundError, ModuleNotFoundError, ValueError) as error:
        st.error(f"Unable to load the trained model: {error}")
        st.stop()

    sample = pd.DataFrame([values], columns=FEATURES.values())
    prediction = model.predict(sample)[0]
    st.subheader(f"Prediction: {prediction}")

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(sample)[0]
        classes = getattr(model, "classes_", [])
        st.write("Prediction confidence")
        st.dataframe(
            pd.DataFrame({"Species": classes, "Probability": probabilities})
            .sort_values("Probability", ascending=False)
            .reset_index(drop=True),
            hide_index=True,
            use_container_width=True,
        )


if __name__ == "__main__":
    main()
