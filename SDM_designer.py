#!/usr/bin/env python
# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Bio import SeqIO
from Bio.Seq import Seq
import math



#関数の設定
#Fasta fileを開く
def open_text():
    if check_v.get():
            text_editor_amino.delete('1.0', tk.END)
            gene = text_editor.get('1.0',tk.END)
            gene = gene.replace('\r','')
            gene = gene.replace('\n','')
            gene = Seq(gene)
            amino = gene.translate()
            text_editor_amino.insert(tk.END, amino)


    else:
        typ = [('Text Files', '*.fasta')]
        filepath = askopenfilename(filetypes=typ)
        entry.insert(tk.END, filepath)
        if not filepath:
            return
        text_editor.delete('1.0', tk.END)
        text_editor_amino.delete('1.0', tk.END)
        #with open(filepath, "r", encoding="utf-8") as open_file:
        #    text = open_file.read()
        #    text_editor.insert(tk.END, text)
        #root.title(f'Text Files - {filepath}')

        with open(filepath) as handle:
            for record in SeqIO.parse(handle, "fasta"):
                gene = record.seq
                gene_name = record.id
            amino = gene.translate()
            text_title["text"] = gene_name
            text_editor.insert(tk.END, gene)
            text_editor_amino.insert(tk.END, amino)


    if check_direct_v.get():
        aminofind_title.place(x=0, y=0, width=200)
        entry_aminofind.place(x=5, y=30, width=130)
        entry_aminofind.config(state='readonly')
        button_aminofind.place(x=135, y=28, width=60)
        button_aminofind.config(state='disabled')
        amino_info.place(x=0, y=55, width=200)
        aminofind_title.place(x=0, y=0, width=200)
        entry_aminofind.place(x=5, y=30, width=130)
        entry_aminofind.config(state='readonly')
        button_aminofind.place(x=135, y=28, width=60)
        button_aminofind.config(state='disabled')
        amino_info.place(x=0, y=55, width=200)

        find_title.place(x=0, y=85, width=200)
        entry_find.place(x=5, y=110, width=130)
        entry_find.config(state='readonly')
        button_find.place(x=135, y=108, width=60)
        button_find.config(state='disabled')
        gene_info.place(x=0, y=135, width=200)

        omake_title.place(x=0, y=170, width=200)
        entry_omake.place(x=5, y=200, width=130)
        entry_omake.config(state='readonly')
        button_omake2.place(x=135, y=198, width=60)
        button_omake2.config(state='disabled')
        button_omake.place(x=0, y=215, width=200)

        text_editor_amino.grid(row=2, column=1)
        text_editor_amino2.grid(row=2, column=1)
        change_title.place(x=0, y=250, width=200)
        entry_change.place(x=5, y=280, width=130)
        entry_change.config(state='readonly')
        button_change.place(x=135, y=278, width=60)
        button_change.config(state='disabled')
        check_direct_title.place(x=0, y=315, width=200)
        entry_check_direct.place(x=5, y=345, width=130)
        entry_check_direct.config(state='normal')
        button_check_direct.place(x=135, y=343, width=60)
        button_check_direct.config(state='abled')
        check_check_direct.place(x=0, y=370, width=200)

        text_title2.grid(row=0,column=1)
        text_editor2.grid(row=1, column=1)

        ali_title.place(x=0, y=0, width=200)
        button_ali_gene.place(x=0, y=30, width=200)
        button_ali_amino.place(x=0, y=60, width=200)
        text_title3.grid(row=0,column=0)
        text_editor_result.grid(row=1, column=0)
        ybar.grid(row=1, column=1,sticky=tk.N + tk.S)
        xbar.grid(row=2, column=0,sticky=tk.W + tk.E)



    else:
        aminofind_title.place(x=0, y=0, width=200)
        entry_aminofind.place(x=5, y=30, width=130)
        entry_aminofind.config(state='normal')
        button_aminofind.place(x=135, y=28, width=60)
        button_aminofind.config(state='abled')
        amino_info.place(x=0, y=55, width=200)
        aminofind_title.place(x=0, y=0, width=200)
        entry_aminofind.place(x=5, y=30, width=130)
        entry_aminofind.config(state='normal')
        button_aminofind.place(x=135, y=28, width=60)
        button_aminofind.config(state='abled')
        amino_info.place(x=0, y=55, width=200)

        find_title.place(x=0, y=85, width=200)
        entry_find.place(x=5, y=110, width=130)
        entry_find.config(state='normal')
        button_find.place(x=135, y=108, width=60)
        button_find.config(state='abled')
        gene_info.place(x=0, y=135, width=200)

        omake_title.place(x=0, y=170, width=200)
        entry_omake.place(x=5, y=200, width=130)
        entry_omake.config(state='normal')
        button_omake2.place(x=135, y=198, width=60)
        button_omake2.config(state='abled')
        button_omake.place(x=0, y=215, width=200)

        text_editor_amino.grid(row=2, column=1)

        change_title.place(x=0, y=250, width=200)
        entry_change.place(x=5, y=280, width=130)
        entry_change.config(state='normal')
        button_change.place(x=135, y=278, width=60)
        button_change.config(state='abled')

        check_direct_title.place(x=0, y=315, width=200)
        entry_check_direct.place(x=5, y=345, width=130)
        entry_check_direct.config(state='readonly')
        button_check_direct.place(x=135, y=343, width=60)
        button_check_direct.config(state='disabled')
        check_check_direct.place(x=0, y=370, width=200)

def change_seq():
    text_editor_amino.delete('1.0', tk.END)
    gene = Seq(text_editor.get('1.0',tk.END))
    amino = gene.translate()
    text_editor_amino.insert(tk.END, amino)

#新しく入力された塩基配列を検索する
def find_myseq():
    text_editor2.delete('1.0', tk.END)
    gene = str(text_editor.get('1.0',tk.END))
    gene = gene.replace('\r','')
    gene = gene.replace('\n','')
    gene = gene.upper()
    find_gene = str(entry_find.get())
    find_gene = find_gene.replace('\r','')
    find_gene = find_gene.replace('\n','')
    find_gene = find_gene.upper()
    change_gene = find_gene.replace('A','-')
    change_gene = change_gene.replace('T','-')
    change_gene = change_gene.replace('C','-')
    change_gene = change_gene.replace('G','-')
    newgene = gene.replace(find_gene,change_gene)
    text_editor2.insert(tk.END, newgene)
    find_number = gene.find(find_gene)
    find_length = len(find_gene)
    find_number2 = find_number+find_length
    gene_info["text"] = "["+str(find_number+1)+"]to["+str(find_number2)+"],["+str(find_length)+"]s"
    #text_editor.selection_range(find_number,find_length)

    if find_number>=0 :
        text_editor.delete('1.0', tk.END)
        text_editor.insert(tk.END,gene[:find_number])
        text_editor.insert(tk.END, gene[find_number:find_number2], 'blue')
        text_editor.insert(tk.END,gene[find_number2:])

    else:
        gene_info["text"] = "Not found."

def find_aminoseq():
    entry_find.delete(0, tk.END)
    amino = str(text_editor_amino.get('1.0',tk.END))
    amino = amino.replace('\r','')
    amino = amino.replace('\n','')
    find_amino =  str(entry_aminofind.get())
    find_amino = find_amino.replace('\r','')
    find_amino = find_amino.replace('\n','')
    find_number = amino.find(find_amino)
    find_length = len(find_amino)
    find_number2 = find_number+find_length
    amino_info["text"] = "["+str(find_number+1)+"]to["+str(find_number2)+"],["+str(find_length)+"]s"
    gene = str(text_editor.get('1.0',tk.END))
    gene = gene.replace('\r','')
    gene = gene.replace('\n','')
    amino_to_gene = gene[find_number*3:find_number2*3]
    entry_find.insert(tk.END, str(amino_to_gene))
    text_title2.grid(row=0,column=1)
    text_editor2.grid(row=1, column=1)

def change_myseq():
    gene = str(text_editor.get('1.0',tk.END))
    gene = gene.replace('\r','')
    gene = gene.replace('\n','')
    find_gene = str(entry_find.get())
    find_gene = find_gene.replace('\r','')
    find_gene = find_gene.replace('\n','')
    find_number = gene.find(find_gene)
    find_length = len(find_gene)
    find_number2 = find_number+find_length
    new = str(entry_change.get())
    new = new.replace('\r','')
    new = new.replace('\n','')
    new_length = len(new)

    if find_length == new_length:
        #change_gene = find_gene.replace('A','-')
        #change_gene = change_gene.replace('T','-')
        #change_gene = change_gene.replace('C','-')
        #change_gene = change_gene.replace('G','-')
        #newgene = text_editor2.get('1.0', tk.END)
        #newgene = newgene.replace(str(change_gene),str(new))
        text_editor2.delete('1.0', tk.END)
        text_editor2.insert(tk.END,gene[:find_number])
        text_editor2.insert(tk.END, new, 'red')
        text_editor2.insert(tk.END,gene[find_number2:])

        newgene_seq = Seq(text_editor2.get('1.0', tk.END))
        newgene_seq = newgene_seq.replace('\r','')
        newgene_seq = newgene_seq.replace('\n','')
        new_amino = newgene_seq.translate()
        text_editor_amino2.delete('1.0', tk.END)
        text_editor_amino2.insert(tk.END, str(new_amino))
        text_editor_amino2.grid(row=2, column=1)
        ali_title.place(x=0, y=0, width=200)
        button_ali_gene.place(x=0, y=30, width=200)
        button_ali_amino.place(x=0, y=60, width=200)
        text_title3.grid(row=0,column=0)
        text_editor_result.grid(row=1, column=0)
        ybar.grid(row=1, column=1,sticky=tk.N + tk.S)
        xbar.grid(row=2, column=0,sticky=tk.W + tk.E)


    else:
        entry_change.delete(0, tk.END)
        messagebox.showinfo("Error","警告："+'\r\n'+"選択配列を新規配列に変更するとインサーションやデリーション、フレームシフト等の問題が生じる可能性が有ります"+'\r\n'+'\r\n'\
        "原因："+'\r\n'+"選択配列と新規配列において、塩基数に差が生じているため"+'\r\n'+'\r\n'\
        "推奨："+'\r\n'+"新規配列の作り直し"+'\r\n'+'\r\n'\
        "*意図的に上記問題を引き起こしたい場合："+'\r\n'+"新規配列を"+find_gene+"の所に直接入力してください")

def check_direct_OriginalToNew():
    if check_check_direct_v.get():
        text_editor_amino2.delete('1.0', tk.END)
        gene = text_editor2.get('1.0',tk.END)
        gene = gene.replace('\r','')
        gene = gene.replace('\n','')
        gene = Seq(gene)
        amino = gene.translate()
        text_editor_amino2.insert(tk.END, amino)

    else:
        typ = [('Text Files', '*.fasta')]
        filepath = askopenfilename(filetypes=typ)
        entry.insert(tk.END, filepath)
        if not filepath:
            return
        text_editor2.delete('1.0', tk.END)
        text_editor_amino2.delete('1.0', tk.END)
            #with open(filepath, "r", encoding="utf-8") as open_file:
            #    text = open_file.read()
            #    text_editor.insert(tk.END, text)
            #root.title(f'Text Files - {filepath}')

        with open(filepath) as handle:
            for record in SeqIO.parse(handle, "fasta"):
                gene = record.seq
                gene_name = record.id
            amino = gene.translate()
            text_title["text"] = gene_name
            text_editor2.insert(tk.END, gene)
            text_editor_amino2.insert(tk.END, amino)





def ali_gene():
    text_editor_result.delete('1.0', tk.END)
    gene = Seq(text_editor.get('1.0',tk.END))
    gene = gene.replace('\r','')
    gene = gene.replace('\n','')
    newgene = Seq(text_editor2.get('1.0',tk.END))
    newgene = newgene.replace('\r','')
    newgene = newgene.replace('\n','')
    gene_list = list(gene)
    newgene_list = list(newgene)
    checklist = list()
    for i in range(len(gene)):
        if gene_list[i] == newgene_list[i]:
            checklist.append("|")
        else:
            checklist.append("*")
    checklist = str(checklist)
    checklist = checklist.replace(" ","")
    checklist = checklist.replace("[","")
    checklist = checklist.replace("]","")
    checklist = checklist.replace("'","")
    checklist = checklist.replace(",","")

    for group in range(math.floor(len(gene)/75)):
        text_editor_result.insert(tk.END, \
        '\n\r'+'a('+str(75*group+1)+')'+'\t'+gene[75*group:75*group+75]+'\t'+'a('+str(75*group+75)+')'\
        +'\n\r'+'\t'+str(checklist[75*group:75*group+75])+'\t'\
        +'\n\r'+'b('+str(75*group+1)+')'+'\t'+newgene[75*group:75*group+75]+'\t'+'b('+str(75*group+75)+')'+'\n\r')

    text_editor_result.insert(tk.END, \
    '\n\r'+'a('+str(75*(group+1)+1)+')'+'\t'+gene[75*(group+1):len(gene)-1]+'\t'+'a('+str(len(gene)-1)+')'\
    +'\n\r'+'\t'+str(checklist[75*(group+1):len(gene)-1])+'\t'\
    +'\n\r'+'b('+str(75*(group+1)+1)+')'+'\t'+newgene[75*(group+1):len(gene)-1]+'\t'+'b('+str(len(gene)-1)+')'+'\n\r')



def ali_amino():
    text_editor_result.delete('1.0', tk.END)
    gene = Seq(text_editor_amino.get('1.0',tk.END))
    gene = gene.replace('\r','')
    gene = gene.replace('\n','')
    newgene = Seq(text_editor_amino2.get('1.0',tk.END))
    newgene = newgene.replace('\r','')
    newgene = newgene.replace('\n','')
    gene_list = list(gene)
    newgene_list = list(newgene)
    checklist = list()
    for i in range(len(gene)):
        if gene_list[i] == newgene_list[i]:
            checklist.append("|")
        else:
            checklist.append("*")
    checklist = str(checklist)
    checklist = checklist.replace(" ","")
    checklist = checklist.replace("[","")
    checklist = checklist.replace("]","")
    checklist = checklist.replace("'","")
    checklist = checklist.replace(",","")

    for group in range(math.floor(len(gene)/75)):
        text_editor_result.insert(tk.END, \
        '\n\r'+'a('+str(75*group+1)+')'+'\t'+gene[75*group:75*group+75]+'\t'+'a('+str(75*group+75)+')'\
        +'\n\r'+'\t'+str(checklist[75*group:75*group+75])+'\t'\
        +'\n\r'+'b('+str(75*group+1)+')'+'\t'+newgene[75*group:75*group+75]+'\t'+'b('+str(75*group+75)+')'+'\n\r')

    text_editor_result.insert(tk.END, \
    '\n\r'+'a('+str(75*(group+1)+1)+')'+'\t'+gene[75*(group+1):len(gene)-1]+'\t'+'a('+str(len(gene)-1)+')'\
    +'\n\r'+'\t'+str(checklist[75*(group+1):len(gene)-1])+'\t'\
    +'\n\r'+'b('+str(75*(group+1)+1)+')'+'\t'+newgene[75*(group+1):len(gene)-1]+'\t'+'b('+str(len(gene)-1)+')'+'\n\r')

def omake_text():
    messagebox.showinfo("omakeの説明","この機能はおまけです。アミノ酸配列から塩基配列を予測することができます。予測にはマウスやヒトで最も発現頻度が高いコドンが選択されます。\
    しかし、計算によって最適化されているわけではないので予想外の問題が生じる可能性があります。\
    あくまでもおまけ機能として大きくアタリを付ける程度の心持で使用してください。")

def omake_change():
    entry_change.delete(0, tk.END)
    amino = str(entry_omake.get())
    amino = amino.replace('\r','')
    amino = amino.replace('\n','')
    newgene = amino.replace("A","$%%")
    newgene = newgene.replace("T","@%%")
    newgene = newgene.replace("C","#$%")
    newgene = newgene.replace("G","$$%")
    newgene = newgene.replace("@","A")
    newgene = newgene.replace("#","T")
    newgene = newgene.replace("%","C")
    newgene = newgene.replace("$","G")
    newgene = newgene.replace("F","TTC")
    newgene = newgene.replace("L","CTG")
    newgene = newgene.replace("I","ATC")
    newgene = newgene.replace("M","ATG")
    newgene = newgene.replace("V","GTG")
    newgene = newgene.replace("P","CCC")
    newgene = newgene.replace("Y","TAC")
    newgene = newgene.replace("H","CAC")
    newgene = newgene.replace("Q","CAG")
    newgene = newgene.replace("N","AAC")
    newgene = newgene.replace("K","AAG")
    newgene = newgene.replace("D","GAC")
    newgene = newgene.replace("E","GAG")
    newgene = newgene.replace("STOP","TGG")
    newgene = newgene.replace("W","TGG")
    newgene = newgene.replace("S","AGC")
    newgene = newgene.replace("R","AGA")
    entry_change.insert(tk.END, str(newgene))

def ALL_reset():
    entry.delete(0, tk.END)
    entry_aminofind.delete(0, tk.END)
    entry_find.delete(0, tk.END)
    amino_info = tk.Label(frame, text="[XX]to[XX],[XX]s")
    gene_info = tk.Label(frame, text="[XX]to[XX],[XX]s")
    entry_change.delete(0, tk.END)
    entry_omake.delete(0, tk.END)
    text_title = tk.Label(frame_basegene,text=u"　")
    text_editor.delete('1.0', tk.END)
    text_editor_amino.delete('1.0', tk.END)
    text_editor2.delete('1.0', tk.END)
    text_editor_amino2.delete('1.0', tk.END)
    text_editor_result.delete('1.0', tk.END)




# rootメインウィンドウの設定
root = tk.Tk()
root.title("gene")
root.geometry()

# メインフレームの作成と設置
frame_height = 100
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
file_title = tk.Label(frame, text="Open the original sequence", font=("Arial", 13), bg='#c9f3ff')
entry = ttk.Entry(frame)
button = ttk.Button(frame, text="open", command=open_text)
check_v = tk.BooleanVar()
check = tk.Checkbutton(frame, \
text='Direct input of sequence data',\
variable=check_v, \
onvalue=True,\
offvalue=False,\
bg='#c9f3ff')
check_direct_v = tk.BooleanVar()
check_direct = tk.Checkbutton(frame, text='Comparison of original and new', \
variable=check_direct_v, \
onvalue=True,\
offvalue=False,\
bg='#c9f3ff')

button_original = ttk.Button(frame, text="変換(amino)", command=change_seq)

#選択したアミノ酸配列からDNA配列の予測
aminofind_title = tk.Label(frame2, text="Enter the target Amino", font=("Arial", 15), bg='#d4ffc9')
entry_aminofind = ttk.Entry(frame2)
button_aminofind = ttk.Button(frame2, text="Search", command=find_aminoseq)
amino_info = tk.Label(frame2, text="[XX]to[XX],[XX]s", bg='#d4ffc9')
#得られたDNA配列をFasata中のデータから検索
find_title = tk.Label(frame2, text="Enter the target Gene", font=("Arial", 15), bg='#d4ffc9')
entry_find = ttk.Entry(frame2)
button_find = ttk.Button(frame2, text="Search", command=find_myseq)
gene_info = tk.Label(frame2, text="[XX]to[XX],[XX]s", bg='#d4ffc9')

change_title = tk.Label(frame2, text="Enter the new Gene", font=("Arial", 15), bg='#d4ffc9')
entry_change = ttk.Entry(frame2)
button_change = ttk.Button(frame2, text="substitution", command=change_myseq)

check_direct_title =  tk.Label(frame2, text="Open the new sequence", font=("Arial", 13), bg='#d4ffc9')
entry_check_direct = ttk.Entry(frame2)
button_check_direct = ttk.Button(frame2, text="open", command=check_direct_OriginalToNew)
check_check_direct_v = tk.BooleanVar()
check_check_direct = tk.Checkbutton(frame2, \
text='Direct input of sequence data',\
variable=check_check_direct_v, \
onvalue=True,\
offvalue=False,\
bg='#d4ffc9')

ali_title = tk.Label(frame3, text="Result Confirmation", font=("Arial", 15), bg='#ffc9c9')
button_ali_gene = ttk.Button(frame3, text="gene_check", command=ali_gene)
button_ali_amino = ttk.Button(frame3, text="amino_check", command=ali_amino)

omake_title = tk.Label(frame2, text="Enter the new Amino", font=("Arial", 15), bg='#d4ffc9')
button_omake = tk.Button(frame2, text="******Caution******", bg='#d4ffc9', relief='flat', fg="blue", command=omake_text)
entry_omake = ttk.Entry(frame2)
button_omake2 = ttk.Button(frame2, text="変換(amino)", command=omake_change)

button_reset = ttk.Button(frame2, text="reset", command=ALL_reset)


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
check_direct.place(x=0, y=75, width=200)

text_title.grid(row=0,column=1)
text_editor.grid(row=1, column=1)

text_editor.tag_configure("blue", foreground="#0000FF")
text_editor2.tag_configure("red", foreground="#FF0000")


ybar.config(command=text_editor_result.yview)
text_editor_result.config(yscrollcommand=ybar.set)
xbar.config(command=text_editor_result.xview)
text_editor_result.config(xscrollcommand=xbar.set)



root.mainloop()
