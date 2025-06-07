class Stub:
    def __init__(self, app_ids):
        self.app_ids = app_ids

    def call(self, app_id, data, user):
        print(f"Stub call to app: {app_id} with data: {data} as user: {user}")

        # For demonstration, we return dummy bytes
        # In real use, this should call the actual Openfabric app API
        if 'prompt' in data:
            return {"result": b"fake_image_binary_data"}
        elif 'image' in data:
            return {"result": b"fake_3d_model_binary_data"}
        else:
            return {"result": b""}
