import logging

extData = {
    'user': 'joem@example.com',
    'password':'qwerty'

}


def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)


def main():
    # set the output file and debug level, and
    # use a custom formatting specification
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s Password:%(password)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p" # 12/31/2009 11:59:59 PM
    logging.basicConfig(filename="output_2.log",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()


if __name__ == "__main__":
    main()
