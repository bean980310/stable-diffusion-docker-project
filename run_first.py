#!/usr/bin/env python
# coding: utf-8
from IPython import get_ipython

# # Run First

# In[1]:


# IMPORTANT: Run this shell before Install Packages and CUDA, cuDNN, Docker, NVIDIA Container toolkit on Jupyter Notebook.
# IMPORTANT: DON'T LEAK YOUR PASSWORD!
from getpass import getpass
import os

def check_passwd():
    if os.path.exists('mypassword'):
        with open('mypassword', 'r') as f:
            passwd=getpass()
            if passwd==f.read():
                return True
            else:
                return False
    else:
        set_passwd()
    
def set_passwd():
     with open('mypassword', 'w') as f:
        passwd=getpass()
        f.write(passwd)

check_passwd()


# ## Install Packages

# In[ ]:


get_ipython().system('sudo -S apt-get update < mypassword')


# In[ ]:


get_ipython().system('sudo -S apt-get install -y build-essential pandoc gcc g++ software-properties-common bash python3-pip python3-tk python3-dev python3-launchpadlib bash git git-lfs net-tools netcat-openbsd ffmpeg wget curl p7zip-full pkg-config ca-certificates jq libglib2.0-0 libsm6 libgl1 libxrender1 libxext6 libcairo2-dev libgoogle-perftools4 libtcmalloc-minimal4 < mypassword')


# In[ ]:


get_ipython().system('sudo -S update-ca-certificates < mypassword')


# ## Install CUDA

# In[ ]:


get_ipython().system('wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-ubuntu2404.pin')


# In[ ]:


get_ipython().system('sudo -S mv cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-repository-pin-600 < mypassword')


# In[ ]:


get_ipython().system('wget https://developer.download.nvidia.com/compute/cuda/12.6.2/local_installers/cuda-repo-ubuntu2404-12-6-local_12.6.2-560.35.03-1_amd64.deb')


# In[ ]:


get_ipython().system('sudo -S dpkg -i cuda-repo-ubuntu2404-12-6-local_12.6.2-560.35.03-1_amd64.deb < mypassword')


# In[ ]:


get_ipython().system('sudo -S cp /var/cuda-repo-ubuntu2404-12-6-local/cuda-*-keyring.gpg /usr/share/keyrings/ < mypassword')


# In[ ]:


get_ipython().system('sudo -S apt-get update < mypassword')


# In[ ]:


get_ipython().system('sudo -S apt-get -y install cuda-12-6 < mypassword')


# ### Install cuDNN

# In[ ]:


get_ipython().system('wget https://developer.download.nvidia.com/compute/cudnn/9.5.0/local_installers/cudnn-local-repo-ubuntu2404-9.5.0_1.0-1_amd64.deb')


# In[ ]:


get_ipython().system('sudo -S dpkg -i cudnn-local-repo-ubuntu2404-9.5.0_1.0-1_amd64.deb < mypassword')


# In[ ]:


get_ipython().system('sudo -S cp /var/cudnn-local-repo-ubuntu2404-9.5.0/cudnn-*-keyring.gpg /usr/share/keyrings/ < mypassword')


# In[ ]:


get_ipython().system('sudo -S apt-get update < mypassword')


# In[ ]:


get_ipython().system('sudo -S apt-get -y install cudnn < mypassword')


# ## Install Conda

# In[ ]:


get_ipython().system('curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh')


# In[ ]:


get_ipython().system('bash ~/Anaconda3-2024.10-1-Linux-x86_64.sh -b -p $HOME/anaconda3')


# In[ ]:


get_ipython().run_line_magic('source', '~/anaconda3/bin/activate')
get_ipython().run_line_magic('conda', 'init --all')


# ## Install Pytorch

# In[ ]:


get_ipython().run_line_magic('pip', 'install torch torchvision torchaudio')


# In[ ]:


get_ipython().run_line_magic('conda', 'install -y pytorch torchvision torchaudio pytorch-cuda=12.4 -c pytorch -c nvidia')


# ## Install Huggingface

# In[ ]:


get_ipython().run_line_magic('pip', 'install huggingface-hub transformers diffusers safetensors tokenizers datasets peft gradio')


# In[ ]:


get_ipython().run_line_magic('conda', 'install -y huggingface_hub transformers safetensors tokenizers datasets -c huggingface')


# In[ ]:


get_ipython().run_line_magic('conda', 'install -y diffusers accelerate sentence-transformers -c conda-forge')


# In[ ]:


get_ipython().run_line_magic('pip', 'install peft gradio')


# ## Install Tensorflow

# In[ ]:


get_ipython().run_line_magic('pip', 'install tensorflow tensorboard tensorboardx')


# ## Install onnxruntime

# In[ ]:


get_ipython().run_line_magic('pip', 'install onnxruntime-gpu onnx')


# ## Install CivitAI Model Downloader

# In[ ]:


get_ipython().run_line_magic('pip', 'install civitai-model-downloader')


# ## configure API key

# In[ ]:


from huggingface_hub import notebook_login

notebook_login()


# In[ ]:


from civitai_downloader import login

login()


# ## Install Docker Engine

# In[ ]:


get_ipython().system('sudo -S install -m 0755 -d /etc/apt/keyrings < mypassword')
get_ipython().system('sudo -S curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc < mypassword')
get_ipython().system('sudo -S chmod a+r /etc/apt/keyrings/docker.asc < mypassword')


# In[ ]:


get_ipython().system('echo    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" |    xargs -a mypassword | sudo -S tee /etc/apt/sources.list.d/docker.list > /dev/null')
get_ipython().system('sudo -S apt-get update < mypassword')


# In[ ]:


get_ipython().system('sudo -S apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin < mypassword')


# In[ ]:


get_ipython().system('sudo -S groupadd docker < mypassword')


# In[ ]:


get_ipython().system('sudo -S usermod -aG docker $USER < mypassword')


# ### Install NVIDIA Container toolkit

# In[ ]:


get_ipython().system("curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo -S gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg < mypassword    && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list |      sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' |      sudo -S tee /etc/apt/sources.list.d/nvidia-container-toolkit.list < mypassword")


# In[ ]:


get_ipython().system("sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list")


# In[ ]:


get_ipython().system('sudo -S apt-get update < mypassword')


# In[ ]:


get_ipython().system('sudo -S apt-get install -y nvidia-container-toolkit < mypassword')


# In[ ]:


get_ipython().system('sudo -S nvidia-ctk runtime configure --runtime=docker < mypassword')


# In[ ]:


get_ipython().system('sudo -S systemctl restart docker < mypassword')

