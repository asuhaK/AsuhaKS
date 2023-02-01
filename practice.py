# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:32:58 2023

@author: 
"""

import tkinter as tk
from tkinter import ttk

"""
メディアボタンの配置


"""

class MyMediaButton(ttk.Frame):
    def __init__(self, master=None, width=200, height=20):
        super().__init__(master)
        self.width = width
        self.height = height
        self.buttons=[]
        # ボタンの表記と説明文
        self.layout_mark = ['■', '<<','||','▶', '>>', '<|','|>']
        self.layout_word = ['停止' ,'逆再生', '一時停止','再生','早送り','コマ戻し','コマ送り']
        
        # 最小サイズ制限
        if self.width < 100:
            self.width = 100
        if self.height < 10:
            self.height = 10 
        # ウィジェットの作成
        self._create_widgets()
        
    # ウィジェットの作成
    def _create_widgets(self):
        # 上段フレーム
        self.frame1 = ttk.Frame(self, width=self.width, height=self.height)
        # 下段フレーム
        self.frame2 = ttk.Frame(self, width=self.width, height=self.height)
        # 構成指定
        self.frame1.grid(column=0, row=0, sticky=(tk.E, tk.W))
        self.frame2.grid(column=0, row=1, sticky=(tk.E, tk.W))
        self.frame1.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)
        
        # 上段フレームにリストをもとにボタンを配置
        self._set_buttons(self.buttons, self.frame1, self.layout_mark)

        # 下段フレームにスケールバーを定義
        self.val = tk.DoubleVar()
        self.scalebar = ttk.Scale(
            self.frame2,
            variable=self.val,
            orient=tk.HORIZONTAL,
            length=self.width -15,
            from_=0,
            to=100,
            command=lambda e: self._change_text())

        # 下段フレームにラベル追加
        self.label1 = ttk.Label(self.frame2 ,width=10, text="0")

        # 下段フレームにウェジットの配置
        self.scalebar.pack(side="left" ,anchor= "c",expand = 1, fill = "x")
        self.label1.pack(side="left" ,anchor= "c",expand = 0)

    # *内部処理
    # フレームに横一列でボタンを配置する
    def _set_buttons(self, buttons, frame, item_list, width=8):
        for x, char in enumerate(item_list, 1):
            button = ttk.Button(frame, width=width,text=char)
            button.grid(column=x, row=0, sticky=(tk.E, tk.W))
            button.columnconfigure(x, weight=1)
            button.rowconfigure(x, weight=0)
            buttons.append(button)

    # *イベント処理
    # 値変更
    def _change_text(self):
        #print('val:%4d' % self.val.get())
        self.label1.configure(text='%4d' % self.get_value())

    # ボタン押し
    def _clicked_button(self,event):
        char = event.widget['text']
        print(self.get_button_index(char))

    # *外部から操作
    # ボタン表記と説明文を取得
    def get_button_layout(self):
        return self.layout_mark, self.layout_word

    # ボタン表記からインデックスを取得
    def get_button_index(self, char):
        return self.layout_mark.index(char)

    # スケールバー値取得
    def get_value(self):
        return self.val.get()

    # スケールバー値セット
    def set_value(self,value):
        self.val.set(value)
        self._change_text()

    # ボタンのイベント用の関数を登録する
    def set_eventfunc_button(self, func, eventIndex=0):
        if eventIndex == 1 :
            for x, button in enumerate(self.buttons, 1):
                # <Button-1>:左クリック
                button.bind('<Button-1>', func)

    # デモ用関数設定
    def defo_functin(self):
        self.set_eventfunc_button(self._clicked_button, 1)


# クラスのデモ
def demo():
    root = tk.Tk()
    app = MyMediaButton(master=root)
    app.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    #デモ用
    app.defo_functin()
    app.mainloop()

# 単体動作
if __name__ == "__main__":
    demo()