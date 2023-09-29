import sys

def error_msg_detail(error,error_detail:sys):
    o1,o2,exc_tb=error_detail.exc_info()
    error_msg="error is occured in python file name [{1}] line num [{2}] error msg[{3}]".format(exc_tb.tb_frame.f_code.co_filename,exc_tb.tb_lineno,str(error))
    return error_msg


class CustomException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        super.__init__(error_msg)
        self.error_msg=error_msg_detail(error_msg,error_detail)

    def __str__(self):
        return self.error_msg
    
if "__name__"=="__main__":
    try:
        10/0
    except Exception as e:
        raise CustomException(e,sys)