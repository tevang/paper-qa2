# Installation
Follow these concise steps to set up a Conda environment with Python 3.12, install Paper-QA2 from PyPI, and configure 
the `run_paperqa2_Py3.12.py` script to run from any location.

## 1. Create and Activate a Conda Environment
Open your terminal and execute the following commands:

```bash
conda create -n paperqa_env python=3.12
conda activate paperqa_env
```

## 2. Upgrade pip and Install Required Packages
Ensure you have the latest version of pip and install the necessary Python packages:

```bash
pip install --upgrade pip
pip install openai
pip install paper-qa
pip install colorama
```

## 3. Set the OpenAI API Key
Create an activation script to set the `OPENAI_API_KEY` environment variable automatically when activating the Conda environment.

```bash
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo "export OPENAI_API_KEY='put key here'" > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```

**⚠️ Important: Replace 'put key here' with your actual OpenAI API key.

## 4. Configure the pqa Command
Add a shell function to your shell profile to run the Paper-QA2 script easily from any location.

Open your shell profile `~/.bashrc` in a text editor.

Add the following function:

```bash
pqa() {
    # Check if the paperqa_env environment is not active
    if [ "$CONDA_DEFAULT_ENV" != "paperqa_env" ]; then
        # Initialize conda for shell scripts
        if [ -f "/opt/anaconda3/etc/profile.d/conda.sh" ]; then
            source "/opt/anaconda3/etc/profile.d/conda.sh"
        else
            echo "Error: conda.sh not found. Check your Anaconda installation path."
            return 1
        fi
        # Activate the environment
        conda activate paperqa_env
    fi
    # Run the Python script with all arguments
    python /home/thomas/PaperQA2_project/run_paperqa2_Py3.12.py "$@"
}
```

📝 Note:

Modify the full paths in the script above to match your Anaconda installation path and the location of your 
`run_paperqa2_Py3.12.py` script.
For example, replace `/opt/anaconda3/etc/profile.d/conda.sh` with the path to your conda.sh file and 
`/home/thomas/PaperQA2_project/run_paperqa2_Py3.12.py` with the actual path to your script.
Save and close the shell profile file.

Reload the shell configuration:

```bash
source ~/.bashrc
```

## 5. Prepare the Scripts Directory and Move the Script
Create the project directory:

```bash
mkdir -p ~/PaperQA2_project
```

Move your `run_paperqa.py` script to the project directory and rename it:

```bash
mv /path/to/your/run_paperqa.py ~/PaperQA2_project/run_paperqa2_Py3.12.py
chmod +x ~/PaperQA2_project/run_paperqa2_Py3.12.py
```

📝 Note: Replace `/path/to/your/run_paperqa.py` with the actual path to your script.

## 6. Add the Scripts Directory to $PATH
Enable running the script from any location by adding the PaperQA2_project directory to your system's `$PATH`.

```bash
echo 'export PATH="$HOME/PaperQA2_project:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## 7. Run the run_paperqa2_Py3.12.py Script
You can now execute the script from any directory using the following command:

```bash
run_paperqa2_Py3.12.py "What are the implications of SITAR for large proteins?" -p "." -a "about 300 words, but can be longer"
```

**🔧 Reminder: Ensure that all full paths in the pqa function and script locations are correctly modified to match 
your system's configuration.
