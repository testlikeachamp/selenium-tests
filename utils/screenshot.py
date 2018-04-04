import time


def take_screenshot(driver):
    f_name = str(round(time.time() * 1000)) + ".png"
    # des_d = "D:\\testlikechamp\\selenium-tests\\screenshots\\"
    des_d = "/tmp/screenshots/"  # the directory must be created beforehand
    des_f = des_d + f_name

    try:
        driver.save_screenshot(des_f)
        print("Screenshots saved to directory --> " + des_f)
    except NotADirectoryError:
        print("Not directory issue")
