# Description

I tried to install the latest Paper-QA2, first through the GitHub repository and then through PyPI. Unfortunately, in 
both cases, the CLI was broken, but the Python API was functioning without problems. That's why I decided to write a 
Python script to emulate the CLI. Of course, it doesn't retain all the command-line options but includes the most 
important ones.

Below I describe how to install it and run a simple example using the included sample PDF file.

My impression of Paper-QA2 is that it answers questions thoroughly without making up stories like ChatGPT. If it 
doesn't know the answer or if it cannot find the answer in the provided papers, it will simply tell you "I don't know 
the answer," which is appreciated. On the other hand, its answers lack general context because they are based only on 
the given papers, not on the prior existing knowledge on which ChatGPT is trained. I also couldn't understand if it can
somehow query an online repository of paper. So far it works for locally downloaded papers which limits its 
context-knowledge.

Another minor flaw is that it requires a separate subscription to the OpenAI API; if you have a subscription to 
ChatGPT, then it's useless for Paper-QA2. Of course, there is an option to install a local LLM, but I didn't dare to 
delve into this adventure. I have already spent enough time making Paper-QA2 work, and besides, I doubt the 
capabilities of the open-source LLM provided as an alternative to OpenAI's API on GitHub of the 
[original distribution](https://github.com/Future-House/paper-qa).


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
