import uuid

# генерация реферальной ссылки (Позже здесь надо добавить реальную ссылку сайта с правильными параметрами)
def generate_ad_link(base_url=""):
    referral_code = str(uuid.uuid4())[:8]  # Генерируем уникальный код из первых 8 символов UUID
    return base_url + referral_code
