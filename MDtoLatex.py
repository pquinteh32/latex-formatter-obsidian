import FreeSimpleGUI as sg
from main import vault_path, md_to_latex_conversion, encoded_image_icon,resource_path
import os,re

sg.theme('DarkPurple4')

treedata = sg.TreeData()

def add_files_in_tree(parent, dirname):
    files = os.listdir(dirname)
    del_value = '.git'
    filtered_files = [item for item in files if item != del_value]
    for f in filtered_files:
        if (re.search('.obsidian',f)==None):
            fullname = os.path.join(dirname, f)
            if os.path.isdir(fullname):            # if it's a folder, add folder and recurse
                treedata.Insert(parent, fullname, f, values=[],icon=encoded_image_icon(resource_path('folder.png')))
                add_files_in_tree(fullname, fullname)
            else:
                treedata.Insert(parent, fullname, f, values=[os.stat(fullname).st_size], icon=encoded_image_icon(resource_path('documents.png')))

add_files_in_tree('',vault_path)


tree = sg.Tree(
    data=treedata,
    key='-DIR_TREE-',
    enable_events=True,
    auto_size_columns=True,
    num_rows=20,
    col0_width=40,
)



layout = [
    [tree],
    [sg.HorizontalSeparator()],
    [sg.Text("File Selected")],
    [sg.Input(size=350,key='-INPUT-')],
    [sg.Button('Submit'), sg.Button('Exit')]

]

window = sg.Window('Latex Tag', layout, finalize=True, size=(400,450), resizable=True, icon=encoded_image_icon(resource_path('write.png')))



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Exit':
        break
    elif event == '-DIR_TREE-':
        if(re.search(r'(\.md)',values['-DIR_TREE-'][0])!=None):
            window['-INPUT-'].update(values['-DIR_TREE-'][0])
            window.refresh()
    elif event == 'Submit':
        if(re.search(r'(\.md)',values['-DIR_TREE-'][0])!=None):
            if sg.popup_yes_no('Do you want to submit selected file for conversion?') == 'Yes':
                md_to_latex_conversion(values['-DIR_TREE-'][0])
        else:
            sg.popup_error('You have to choose a markdown file, not a text file or directory')