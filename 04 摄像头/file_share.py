from filestack import Client


class FileShare:
    def __init__(self, filepath, api_key='Axdhdku3TgmzurOb8siGYz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        file_link = client.upload(filepath=self.filepath)
        return file_link.url


if __name__ == '__main__':
    file = FileShare('files/20230801-102412.png')
    print(file.share())
