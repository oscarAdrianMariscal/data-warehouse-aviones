
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._label5 = System.Windows.Forms.Label()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._ayudaToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._salirToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._conectar = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self._pictureBox1.BeginInit()
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightYellow
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(261, 156)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Login"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(406, 156)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(124, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightYellow
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(261, 211)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Password"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(406, 211)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(124, 20)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightYellow
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(261, 263)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "DB"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(406, 263)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(124, 20)
		self._textBox3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightYellow
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(261, 316)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "Driver"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(406, 319)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(124, 20)
		self._textBox4.TabIndex = 7
		# 
		# pictureBox1
		# 
		self._pictureBox1.Location = System.Drawing.Point(34, 76)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(198, 271)
		self._pictureBox1.TabIndex = 8
		self._pictureBox1.TabStop = False
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft YaHei UI", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(250, 73)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(217, 43)
		self._label5.TabIndex = 9
		self._label5.Text = "Conexion remota"
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._ayudaToolStripMenuItem,
			self._salirToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(777, 24)
		self._menuStrip1.TabIndex = 10
		self._menuStrip1.Text = "menuStrip1"
		# 
		# ayudaToolStripMenuItem
		# 
		self._ayudaToolStripMenuItem.Name = "ayudaToolStripMenuItem"
		self._ayudaToolStripMenuItem.Size = System.Drawing.Size(53, 20)
		self._ayudaToolStripMenuItem.Text = "Ayuda"
		# 
		# salirToolStripMenuItem
		# 
		self._salirToolStripMenuItem.Name = "salirToolStripMenuItem"
		self._salirToolStripMenuItem.Size = System.Drawing.Size(41, 20)
		self._salirToolStripMenuItem.Text = "Salir"
		# 
		# conectar
		# 
		self._conectar.BackColor = System.Drawing.Color.SkyBlue
		self._conectar.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
		self._conectar.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._conectar.Location = System.Drawing.Point(406, 379)
		self._conectar.Name = "conectar"
		self._conectar.Size = System.Drawing.Size(124, 31)
		self._conectar.TabIndex = 11
		self._conectar.Text = "Conectar"
		self._conectar.UseVisualStyleBackColor = False
		self._conectar.Click += self.ConectarClick
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.SkyBlue
		self._label6.Location = System.Drawing.Point(250, 107)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(498, 23)
		self._label6.TabIndex = 12
		# 
		# Form1
		# 
		self.BackColor = System.Drawing.Color.AliceBlue
		self.ClientSize = System.Drawing.Size(777, 467)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._conectar)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.Name = "Form1"
		self.Text = "DB"
		self._pictureBox1.EndInit()
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def ConectarClick(self, sender, e):
		pass