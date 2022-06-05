from selenium import webdriver
from time import sleep
import os


def click_cell(driver, i):
    '''上からi番目のセルを選択（1始まり）'''
    driver.find_element_by_xpath(
        '//div[@id="notebook-container"]/div[{}]/div[@class="input"]'.format(i)
    ).click()


def click_execute(driver):
    '''jupyterの実行ボタンをクリック'''
    driver.find_element_by_xpath(
        '//button[@data-jupyter-action="jupyter-notebook:run-cell-and-select-next"]'
    ).click()


def fileupload(driver, filepath, i):
    '''
    ファイルアップロードボタンからファイルアップロード
    （i番目のセルのoutputにボタンが複数ある場合は全ての要素に対して処理）
    
    i: int
        アップロードボタンが存在するJupyterセルが上から何番目か（1始まり）
    '''
    driver.find_element_by_xpath(
        '//div[@id="notebook-container"]/div[{}]/div[@class="output_wrapper"]//button'.format(i)
    # ).send_keys(filepath)
    ).click()


def click_filelink(driver, i):
    '''
    ダウンロードリンクからファイルをダウンロード
    （i番目のセルのoutputにリンクが複数ある場合は全ての要素に対して処理）
    
    i: int
        アップロードボタンが存在するJupyterセルが上から何番目か（1始まり）
    '''
    driver.find_element_by_xpath(
        '//div[@id="notebook-container"]/div[{}]/div[@class="output_wrapper"]//a'.format(i)
    ).click()



if __name__ == '__main__':
    # ノートブックを開く
    driver = webdriver.Chrome(executable_path='./libs/chromedriver.exe')
    host = 'http://[IP]:[PORT]'
    driver.get(host + '/jupyter/notebooks/dbtest.ipynb')

    # ファイルアップロードまで
    sleep(3)
    click_cell(driver, 1)
    sleep(1)
    click_execute(driver)
    sleep(2)
    click_execute(driver)
    sleep(2)
    fileupload(driver, os.path.join('data', 'test.csv'), 2)

    # アップロード後、ファイルダウンロードまで
    sleep(20)
    click_cell(driver, 3)
    sleep(1)
    click_execute(driver)
    sleep(2)
    click_execute(driver)
    sleep(2)
    click_execute(driver)
    sleep(2)
    click_filelink(driver, 5)