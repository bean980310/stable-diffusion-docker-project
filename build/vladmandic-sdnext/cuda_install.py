import installer

def install(torch_cmd):
    installer.install(torch_cmd, 'torch torchvision', quiet=True)
    installer.install('onnxruntime-gpu', 'onnxruntime-gpu', ignore=True)
    installer.install('onnx', 'onnx', ignore=True)