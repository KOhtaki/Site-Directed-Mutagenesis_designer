#!/usr/bin/env python
# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename


# rootメインウィンドウの設定
root = tk.Tk()
root.title("gene")
root.geometry()

frame_height = 200
frame2_height = 400
frame3_height = 100

frame2_y = frame_height+10
frame3_y = frame2_y + frame2_height + 5


# メインフレームの作成と設置
frame = tk.Frame(root,bg='#c9f3ff')
frame.place(x=5, y=5, width=200, height=frame_height)
frame2 = tk.Frame(root, bg='#d4ffc9')
frame2.place(x=5, y=frame2_y, width=200, height=frame2_height)
frame3 = tk.Frame(root, bg='#ffc9c9')
frame3.place(x=5, y=frame3_y, width=200, height=frame3_height)
frame_basegene = ttk.Frame(root)
frame_basegene.place(x=205, y=5, width=550, height=1000)
frame_newgene = ttk.Frame(root)
frame_newgene.place(x=745, y=5, width=550, height=1000)
frame_check = ttk.Frame(root)
frame_check.place(x=1285, y=5, width=650, height=1100)

# 各種ウィジェットの作成
#空行の作成
no_text = tk.Label(frame,text=u" ")
no_text2 = tk.Label(frame,text=u" ")
no_text3 = tk.Label(frame,text=u" ")
no_text4 = tk.Label(frame,text=u" ")
no_text5 = tk.Label(frame,text=u" ")
#Fasta fileの検索
file_title = tk.Label(frame, text="Enter your data", font=("Arial", 15), bg='#c9f3ff')
entry = ttk.Entry(frame)
button = ttk.Button(frame, text="open")
check = tk.Checkbutton(frame, text='Direct input of sequence data', bg='#c9f3ff')

#選択したアミノ酸配列からDNA配列の予測
aminofind_title = tk.Label(frame2, text="Enter the target Amino", font=("Arial", 15), bg='#d4ffc9')
entry_aminofind = ttk.Entry(frame2)
button_aminofind = ttk.Button(frame2, text="Search")
amino_info = tk.Label(frame2, text="[XX]to[XX],[XX]s", bg='#d4ffc9')
#得られたDNA配列をFasata中のデータから検索
find_title = tk.Label(frame2, text="Enter the target Gene", font=("Arial", 15), bg='#d4ffc9')
entry_find = ttk.Entry(frame2)
button_find = ttk.Button(frame2, text="Search")
gene_info = tk.Label(frame2, text="[XX]to[XX],[XX]s", bg='#d4ffc9')

change_title = tk.Label(frame2, text="Enter the new Gene", font=("Arial", 15), bg='#d4ffc9')
entry_change = ttk.Entry(frame2)
button_change = ttk.Button(frame2, text="substitution")

ali_title = tk.Label(frame3, text="Result Confirmation", font=("Arial", 15), bg='#ffc9c9')
button_ali_gene = ttk.Button(frame3, text="gene_check")
button_ali_amino = ttk.Button(frame3, text="amino_check")

omake_title = tk.Label(frame2, text="Enter the new Amino", font=("Arial", 15), bg='#d4ffc9')
button_omake = tk.Button(frame2, text="******Caution******", bg='#d4ffc9', relief='flat', fg="blue")
entry_omake = ttk.Entry(frame2)
button_omake2 = ttk.Button(frame2, text="conversion")

button_reset = ttk.Button(frame, text="reset")


text_title = tk.Label(frame_basegene,text=u"　")
text_editor = tk.Text(frame_basegene, height=30, width=75)
text_editor_amino = tk.Text(frame_basegene, height=30, width=75)
text_title2 = tk.Label(frame_newgene,text="new seq")
text_editor2 = tk.Text(frame_newgene, height=30, width=75)
text_editor_amino2 = tk.Text(frame_newgene, height=30, width=75)
text_title3 = tk.Label(frame_check,text="result space")
text_editor_result = tk.Text(frame_check, height=58, width=85, wrap=tk.NONE)
ybar = tk.Scrollbar(frame_check, orient=tk.VERTICAL)
xbar = tk.Scrollbar(frame_check, orient=tk.HORIZONTAL)

# 各種ウィジェットの設置
file_title.place(x=0, y=0, width=200)
entry.place(x=5, y=30, width=130)
button.place(x=135, y=28, width=60)
check.place(x=0, y=55, width=200)

aminofind_title.place(x=0, y=0, width=200)
entry_aminofind.place(x=5, y=30, width=130)
button_aminofind.place(x=135, y=28, width=60)
amino_info.place(x=0, y=55, width=200)

find_title.place(x=0, y=85, width=200)
entry_find.place(x=5, y=110, width=130)
button_find.place(x=135, y=108, width=60)
gene_info.place(x=0, y=135, width=200)

omake_title.place(x=0, y=170, width=200)
entry_omake.place(x=5, y=200, width=130)
button_omake2.place(x=135, y=198, width=60)
button_omake.place(x=0, y=215, width=200)

change_title.place(x=0, y=250, width=200)
entry_change.place(x=5, y=280, width=130)
button_change.place(x=135, y=278, width=60)

ali_title.place(x=0, y=0, width=200)
button_ali_gene.place(x=0, y=30, width=200)
button_ali_amino.place(x=0, y=60, width=200)


#button_reset.grid(row=20, column=1)
#button_reset.grid(row=20, column=1)

text_title.grid(row=0,column=1)
text_editor.grid(row=1, column=1)
text_editor_amino.grid(row=2, column=1)
text_title2.grid(row=0,column=1)
text_editor2.grid(row=1, column=1)
text_editor_amino2.grid(row=2, column=1)
text_title3.grid(row=0,column=0)
text_editor_result.grid(row=1, column=0)
ybar.grid(row=1, column=1,sticky=tk.N + tk.S)
xbar.grid(row=2, column=0,sticky=tk.W + tk.E)


text_editor.tag_configure("blue", foreground="#0000FF")
text_editor2.tag_configure("red", foreground="#FF0000")


ybar.config(command=text_editor_result.yview)
text_editor_result.config(yscrollcommand=ybar.set)
xbar.config(command=text_editor_result.xview)
text_editor_result.config(xscrollcommand=xbar.set)



root.mainloop()
