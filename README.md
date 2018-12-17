# Blue-Chip
เราวิเคราะห์ตลาดหุ้น 5 หุ้นที่น่าจับตามอง ถึงการขยายตัว หดตัว และความน่าสนใจที่จะลงทุน

## เราทำอะไร
เรานำข้อมูลหุ้นตัวอย่างจำนวน 5 หุ้นจาก yahoo finance ตั้งแต่วันที่ 20/5/2018-20/11/2018 มาวิเคราะห์
จาก closing price, adj. close, volume.
1. วิเคราะห์จังหวะขึ้นลงของหุ้นและหาข่าวเกี่ยวกับบริษัทหุ้นในช่วงเหล่านั้นว่าเกิดเหตุการณ์อะไรที่ทำให้ทิศทางหุ้น ขึ้น-ลง ตามข้อมูล
2. วิเคราะห์ ราคาปิด และดูว่าหุ้นแต่ละตัวมีจำนวนครั้งที่สูงขึ้นหรือต่ำลงจากวันก่อนหน้า และ สูงกว่าหรือต่ำหว่าค่าเฉลี่ยของหุ้นนั้นๆเป็นจำนวนกี่ครั้งและวิเคราะห์ความน่าลงทุน
3. วิเคราะห์ จำนวนหุ้นที่ขายออกในแต่ละวันและดูว่าหุ้นตัวไหนมีจำนวนที่ขายออกสูง-ต่ำที่สุดและจัดลำดับความนิยม
4. ลองทำ Pair trade ของหุ้นตัวอย่าง 2 ตัวจาก adj. close ว่าควรซื้อขายหุ้นควบคู่ 2 ตัวนั้นเมื่อถึงราคาเท่าไรและอย่างไร

## ข้อมูลที่นำมาวิจัย
 - ผู้วิจัยใช้ข้อมูลจาก Yahoo Finance ซึ่งเป็นข้อมูลหุ้นตัวอย่างจาก 5 บริษัท คือ 
   Apple, HP Inc, Intel Corporation, Microsoft Corporation, Google
   ขนาด 49 KB

## 3rd Party Libraries และ modules
 - matplotlip 2.2.3
 - numpy 1.15.4
 - pandas 0.23.4

## Output
ข้อมูลที่ถูกดึงมาใช้ประมวลผลจะเก็บในรูปแบบ list หลังจากนั้นจึงนำมาแสดงผลเป็นกราฟผ่าน graph.py

## ผลลัพธ์
ผลลัพธ์งานวิจัยได้ถูกแสดงไว้บนเว็บไซต์ของเรา https://www.it.kmitl.ac.th/~it61070210/PSIT/Blue%20Chip.html
link Youtube : https://www.youtube.com/watch?v=0W131bBv1ag&t=410s

Blue Chip Team
