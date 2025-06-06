from sdk.schema.schema import AppModel, InputClass, OutputClass
from sdk.helper import configurations
from sdk.wrapper import Stub
from memory import MemoryManager
import os
import logging

logging.basicConfig(level=logging.INFO)

def execute(model: AppModel) -> None:
    request: InputClass = model.request
    user_config = configurations.get('super-user', None)

    app_ids = user_config['app_ids'] if user_config else []
    stub = Stub(app_ids)

    prompt = request.prompt
    logging.info(f"Received prompt: {prompt}")

    # Step 1: Use local LLM (simulate prompt expansion)
    expanded_prompt = f"Creative expansion of: {prompt}"

    # Step 2: Call Text-to-Image app
    text_to_image_app_id = app_ids[0] if len(app_ids) > 0 else None
    if text_to_image_app_id is None:
        raise Exception("Text-to-Image app ID missing")

    text_to_image_response = stub.call(text_to_image_app_id, {'prompt': expanded_prompt}, 'super-user')
    image_bytes = text_to_image_response.get('result')

    # Save image to file
    os.makedirs('generated', exist_ok=True)
    image_path = os.path.join('generated', 'output.png')
    with open(image_path, 'wb') as f:
        f.write(image_bytes)

    logging.info(f"Image saved to {image_path}")

    # Step 3: Call Image-to-3D app
    image_to_3d_app_id = app_ids[1] if len(app_ids) > 1 else None
    if image_to_3d_app_id is None:
        raise Exception("Image-to-3D app ID missing")

    image_to_3d_response = stub.call(image_to_3d_app_id, {'image': image_bytes}, 'super-user')
    model_bytes = image_to_3d_response.get('result')

    # Save 3D model to file
    model_path = os.path.join('generated', 'model.obj')
    with open(model_path, 'wb') as f:
        f.write(model_bytes)

    logging.info(f"3D model saved to {model_path}")

    # Step 4: Save prompt and results to memory (SQLite)
    memory = MemoryManager('memory.db')
    memory.save_prompt_result(prompt, expanded_prompt, image_path, model_path)
    logging.info("Saved prompt and results to memory")

    # Prepare response message
    response: OutputClass = model.response
    response.message = f"Prompt processed. Image saved at {image_path}, 3D model saved at {model_path}."
