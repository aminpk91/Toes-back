def model_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / related title/<filename>
    file_type = filename.split('.')[-1]
    filename = filename.split('.')[0]
    return f'{instance.related_title}/{filename}.{file_type}'


def Subject_image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / related title/<filename>
    file_type = filename.split('.')[-1]
    filename = filename.split('.')[0]
    return f'{instance.title}/{filename}.{file_type}'
