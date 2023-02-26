import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import logging
import requests
# Handler for /start command
def start(update:Update, context:CallbackContext):

    update.message.reply_text('Botga rasm yuboring uni kanalga baholash uchun jo\'natadi.')

# Handler for get image
def get_image(update:Update, context:CallbackContext):
    """
    Get the image from the user and send to backend
    """
    # Get the message id
    message_id = update.message.message_id
    # Get image id
    image_id = update.message.photo[-1].file_id
    # Print message id and image id to the log

    print(f"Message id: {message_id}, Image id: {image_id}")
    # Send image to backend
    # endpoint url
    url = 'http://rystambek.pythonanywhere.com/api/addImage'
    # Payload
    payload = {
        'message_id': message_id,
        'image_id': image_id
    }
    # Send request
    response = requests.post(url, json=payload)
    # Print status code
    print(response.status_code)
    data = requests.get(f"http://rystambek.pythonanywhere.com/api/{message_id}").json()
    likes = data['like']
    dislikes = data['dislike']
    keyboard = InlineKeyboardMarkup([
        [
        InlineKeyboardButton(f"👍 {likes}", callback_data=f'like {message_id}'),
        InlineKeyboardButton(f"👎 {dislikes}", callback_data=f'dislike {message_id}')
        
        ]
    ])


    
    channel_id = '@Rustambek03_IT_blog'
    # Send image to channel
    context.bot.send_photo(
        chat_id=channel_id, 
        photo=image_id,
        caption="Like this image to get 10 likes back",
        reply_markup=keyboard
        )
    

def callback_like(update:Update, context:CallbackContext):
    query = update.callback_query
    # Get query data
    like,image_id = query.data.split(' ')
    #  Get user id
    user_id = query.from_user.id
    # Get message id
    message_id = query.message.message_id
    if like == "like":
        url = 'https://rystambek.pythonanywhere.com/api/add-like/'
        payload = {
            'user_id': user_id,
            'image_id': image_id
        }
        # Send request
        response = requests.post(url, json=payload)
        # Print status code
        print(response.json())
    if like == "dislike":
        url = 'https://rystambek.pythonanywhere.com/api/add-dislike/'
        payload = {
            'user_id': user_id,
            'image_id': image_id
        }
        # Send request
        response = requests.post(url, json=payload)
        # Print status code
        print(response.status_code)

    url = f'http://rystambek.pythonanywhere.com/api/{image_id}'
        
    # Send request
    response = requests.get(url)
    data = response.json()
    likes = data['like']
    dislikes = data['dislike']
    keyboard = InlineKeyboardMarkup([
        [
        InlineKeyboardButton(f"👍 {likes}", callback_data=f'like {image_id}'),
        InlineKeyboardButton(f"👎 {dislikes}", callback_data=f'dislike {image_id}')
        ]
    ])
    channel_id = '@Rustambek03_IT_blog'
    # Send image to channel
    context.bot.edit_message_reply_markup(
        chat_id=channel_id, 
        message_id = message_id,
        reply_markup=keyboard
        )

        
    query.answer(
        query.edit_message_text(text="Selected option: {}".format(like))
        )
    # query.edit_message_text(text="Selected option: {}".format(query.data.split(":")[0]))

    