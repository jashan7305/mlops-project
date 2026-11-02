# Iris classifier

This project serves the saved Extra Trees Iris model with Streamlit.

## Run locally

```bash
streamlit run main.py
```

Open <http://localhost:8501> and adjust the measurements in the sidebar.

## Run with Docker Compose

```bash
docker compose up --build
```

The app is then available at <http://localhost:8501>.

## Deploy on Streamlit Community Cloud

The deployment pipeline is in [.github/workflows/ci.yml](.github/workflows/ci.yml).
Because Streamlit Community Cloud deploys directly from GitHub, the first deployment
must be connected once:

1. Push this repository to GitHub.
2. In [Streamlit Community Cloud](https://share.streamlit.io/), choose **Create app**.
3. Select this repository, the `main` branch, and `main.py`, then deploy.
4. In the GitHub repository settings, create a repository variable named
   `STREAMLIT_APP_URL` containing the public app URL, for example
   `https://iris-mlops-project.streamlit.app/`.
5. If desired, protect the `production` GitHub environment with a required approval.

After this one-time setup, every push to `main` runs the tests and Docker build.
If they pass, Streamlit Community Cloud automatically redeploys the connected app
from the new commit. The final workflow job polls `/_stcore/health` and fails if
the deployed app does not become healthy.

The model file in `models/iris_extra_trees_model.joblib` is loaded at startup.
