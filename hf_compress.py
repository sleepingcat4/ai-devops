import subprocess

def convert_to_gguf():
    model_dir = input("Enter the path to the model directory: ").strip()
    output_name = input("Enter the output filename (e.g., Qwen2_Math_1.5B.gguf): ").strip()
    outtype = input("Enter the output type (default is q8_0): ").strip() or "q8_0"
    script_path = input("Enter the path to the Python conversion script: ").strip()
    
    cmd = [
        "python3",
        script_path,
        model_dir,
        "--outfile", output_name,
        "--outtype", outtype
    ]
    
    subprocess.run(cmd, check=True)
