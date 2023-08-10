from fastapi import FastAPI, UploadFile, File, status
from app.DataPreprocessing.processing_utils import process_input_image
from app.Prediction.predict import predict_emotion
import tensorflow as tf
from fastapi.responses import JSONResponse


model = tf.keras.models.load_model("app/Models_artifacts/Model1")

app = FastAPI()


@app.post('/predict', summary="Return emotion prediction")
async def predict_emotions(image_file: UploadFile = File(...)):
    """When you see the await keyword, it's like telling your code, 
    "Hey, I'm waiting for this slow task to finish, but in the meantime, you can do other stuff."""

    processed_image = await process_input_image(image_file.file)
    predicted_class, score = await predict_emotion(processed_image, model)

    message = f"This image most likely belongs to {predicted_class} with a {round(score)}% confidence."

    return JSONResponse(content={"status": status.HTTP_200_OK,
                                 "message":  message,
                                 "data": {"class": predicted_class}},
                        status_code=status.HTTP_200_OK,
                        )
