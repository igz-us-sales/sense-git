from module import external_function

def handler(context):
    context.logger.info(external_function())
