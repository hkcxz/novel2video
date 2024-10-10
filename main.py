from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

from backend_py.rest_handler.character import get_local_characters, get_new_characters, get_random_appearance, put_characters
from backend_py.rest_handler.image import generate_images, get_local_images
from backend_py.rest_handler.inital import get_initial, get_novel_fragments, save_combined_fragments
from backend_py.rest_handler.prompt import extract_scene_from_texts, get_prompts_en, save_prompt_en
from backend_py.tts.tts import generate_audio_files
from backend_py.util.constant import ImageDir

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s [File: %(filename)s, Line: %(lineno)d]'
)

# novel 
@app.route('/api/get/novel/fragments', methods=['GET'])
def api_get_novel_fragments():
    return get_novel_fragments()

@app.route('/api/save/novel/fragments', methods=['POST'])
def api_save_combined_fragments():
    return save_combined_fragments()

# prompts
@app.route('/api/get/novel/prompts', methods=['GET'])
def api_extract_scene_from_texts():
    return extract_scene_from_texts()

@app.route('/api/novel/prompts/en', methods=['GET'])
def api_get_prompts_en():
    return get_prompts_en()

@app.route('/api/novel/prompt/en', methods=['POST'])
def api_save_prompt_en():
    return save_prompt_en()

# image
@app.route('/api/novel/images', methods=['POST'])
def api_generate_image():
    return generate_images()

@app.route('/api/novel/images', methods=['GET'])
def api_get_local_images():
    return get_local_images()


# 初始化
@app.route('/api/novel/initial', methods=['GET'])
def api_get_initial():
    return get_initial()

# tts
@app.route('/api/novel/audio', methods=['POST'])
def api_generate_audio_files():
    return generate_audio_files()

# character
@app.route('/api/novel/characters', methods=['GET'])
def api_get_new_characters():
    return get_new_characters()

@app.route('/api/novel/characters/local', methods=['GET'])
def api_get_local_characters():
    return get_local_characters()

@app.route('/api/novel/characters', methods=['PUT'])
def api_put_characters():
    return put_characters()

@app.route('/api/novel/characters/random', methods=['GET'])
def api_get_random_appearance():
    return get_random_appearance()

if __name__ == '__main__':
    app.run(host='localhost', port=1198)