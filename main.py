from sdk.schema.schema import AppModel, InputClass, OutputClass
from sdk.helper import configurations
from sdk.wrapper import Stub

from local_llm import LocalLLM
from memory import MemoryManager, PromptMemory

import os
import logging

logging.basicConfig(level=logging.INFO)

def is_prompt_blank(prompt):
    return not prompt or prompt.strip() == ''

def mock_expand(prompt):
    return prompt + " ...this is a mock expanded prompt for testing."

# ✅ OpenFabric Flow Entry Point
def execute(model: AppModel) -> None:
    request: InputClass = model.request
    user_config = configurations.get('super-user', None)

    app_ids = user_config['app_ids'] if user_config else []
    stub = Stub(app_ids)

    prompt = request.prompt
    logging.info(f"Received prompt: {prompt}")

    try:
        llm = LocalLLM()
        expanded_prompt = llm.expand(prompt)
    except Exception as e:
        logging.warning(f"Local LLM failed, using mock: {e}")
        expanded_prompt = mock_expand(prompt)

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

    model_path = os.path.join('generated', 'model.obj')
    with open(model_path, 'wb') as f:
        f.write(model_bytes)
    logging.info(f"3D model saved to {model_path}")

    # Step 4: Save to SQLite
    memory = MemoryManager('memory.db')
    memory.save_prompt_result(prompt, expanded_prompt, image_path, model_path)
    logging.info("Saved prompt and results to memory")

    # Respond to user
    response: OutputClass = model.response
    response.message = f"Prompt processed. Image saved at {image_path}, 3D model saved at {model_path}."


# ✅ Local CLI Testing
def main():
    print("Starting AI Developer Challenge App...")

    memory = PromptMemory(max_history=5)

    try:
        llm = LocalLLM()
        use_mock = False
        print("Loaded local LLM successfully.")
    except Exception as e:
        print(f"Failed to load local LLM: {e}")
        use_mock = True

    # Initialize app configuration (simulate OpenFabric setup)
    from sdk.helper import configurations
    from sdk.wrapper import Stub

    user_config = configurations.get('super-user', None)
    app_ids = user_config['app_ids'] if user_config else []
    stub = Stub(app_ids)

    while True:
        user_prompt = input("\nEnter your prompt (or type 'exit' to quit): ")

        if user_prompt.lower() in ['exit', 'quit']:
            print("Exiting...")
            break

        if is_prompt_blank(user_prompt):
            print("Prompt is empty. Please enter some text.")
            continue

        memory.add_prompt(user_prompt)

        if use_mock:
            expanded = mock_expand(user_prompt)
        else:
            expanded = llm.expand(user_prompt)

        print("\nExpanded prompt:\n", expanded)

        # Step 2: Call text-to-image
        text_to_image_app_id = app_ids[0] if len(app_ids) > 0 else None
        if text_to_image_app_id is None:
            print("❌ Text-to-Image app ID missing in config.")
            continue

        text_to_image_response = stub.call(text_to_image_app_id, {'prompt': expanded}, 'super-user')
        image_bytes = text_to_image_response.get('result')

        # Save image
        os.makedirs('generated', exist_ok=True)
        image_path = os.path.join('generated', 'output.png')
        with open(image_path, 'wb') as f:
            f.write(image_bytes)
        print(f"✅ Image saved to {image_path}")

        # Step 3: Call image-to-3D
        image_to_3d_app_id = app_ids[1] if len(app_ids) > 1 else None
        if image_to_3d_app_id is None:
            print("❌ Image-to-3D app ID missing in config.")
            continue

        image_to_3d_response = stub.call(image_to_3d_app_id, {'image': image_bytes}, 'super-user')
        model_bytes = image_to_3d_response.get('result')

        model_path = os.path.join('generated', 'model.obj')
        with open(model_path, 'wb') as f:
            f.write(model_bytes)
        print(f"✅ 3D model saved to {model_path}")

        # Step 4: Save to SQLite memory
        memory_db = MemoryManager('memory.db')
        memory_db.save_prompt_result(user_prompt, expanded, image_path, model_path)
        print("💾 Prompt and results saved to memory.")

        # Final message
        print(f"\n✅ Full pipeline complete for: {user_prompt}")
        print("\nPrompt history preview:")
        for idx, p in enumerate(memory.preview_history(), 1):
            print(f"{idx}: {p}")

if __name__ == "__main__":
    main()
