#!/usr/bin/env python
# coding: utf-8

# ## Run Compose

# In[ ]:
from IPython import get_ipython

get_ipython().system('docker compose up -d stable-diffusion-webui')


# In[ ]:


get_ipython().system('docker compose up -d comfyui')


# In[ ]:


get_ipython().system('docker compose up -d open-webui')


# In[ ]:


get_ipython().system('docker compose up -d kohya_ss')


# In[ ]:


get_ipython().system('docker compose up -d invokeai')


# In[ ]:


get_ipython().system('docker compose up -d fooocus')


# In[ ]:


get_ipython().system('docker compose up -d stable-diffusion-webui-forge')


# In[ ]:


get_ipython().system('docker compose up -d sdnext')


# In[ ]:


get_ipython().system('docker compose up -d easy-diffusion')


# In[ ]:


get_ipython().system('docker compose up -d swarmui')


# In[ ]:


get_ipython().system('docker compose up -d facefusion')


# In[ ]:


get_ipython().system('docker compose up -d omost')


# In[ ]:


get_ipython().system('docker compose up -d stable-audio-tools')


# In[ ]:


get_ipython().system('docker compose up -d audiocraft_plus')


# ## Build Compose

# In[ ]:


get_ipython().system('docker compose build stable-diffusion-webui')


# In[ ]:


get_ipython().system('docker compose build comfyui')


# In[ ]:


get_ipython().system('docker compose build open-webui')


# In[ ]:


get_ipython().system('docker compose build kohya_ss')


# In[ ]:


get_ipython().system('docker compose build invokeai')


# In[ ]:


get_ipython().system('docker compose build fooocus')


# In[ ]:


get_ipython().system('docker compose build stable-diffusion-webui-forge')


# In[ ]:


get_ipython().system('docker compose build sdnext')


# In[ ]:


get_ipython().system('docker compose build easy-diffusion')


# In[ ]:


get_ipython().system('docker compose build swarmui')


# In[ ]:


get_ipython().system('docker compose build facefusion')


# In[ ]:


get_ipython().system('docker compose build omost')


# In[ ]:


get_ipython().system('docker compose build stable-audio-tools')


# In[ ]:


get_ipython().system('docker compose build audiocraft_plus')

