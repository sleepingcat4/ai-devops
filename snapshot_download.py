### downloading model snapshot
from huggingface_hub import snapshot_download

def download_model():
    model_id = input("Enter the model ID (e.g., microsoft/Phi-3-mini-128k-instruct): ").strip()
    local_dir = input("Enter the local directory to save the model: ").strip()
    snapshot_download(repo_id=model_id, local_dir=local_dir)

download_model()
