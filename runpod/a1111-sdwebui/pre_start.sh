# echo "**** syncing venv to workspace, please wait. This could take a while on first startup! ****"
# rsync --remove-source-files -rlptDu --ignore-existing /venv/ /app/venv/

# echo "**** syncing stable diffusion to workspace, please wait ****"
# rsync --remove-source-files -rlptDu --ignore-existing /stable-diffusion-webui/ /app/stable-diffusion-webui/
# ln -s /sd-models/* /app/stable-diffusion-webui/models/Stable-diffusion/
# ln -s /cn-models/* /app/stable-diffusion-webui/extensions/sd-webui-controlnet/models/

if [[ $RUNPOD_STOP_AUTO ]]
then
    echo "Skipping auto-start of webui"
else
    echo "Started webui through relauncher script"
    cd /app/stable-diffusion-webui
    python relauncher.py &
fi
