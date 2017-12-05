import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._usuario = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._password = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._menuStrip1 = System.Windows.Forms.MenuStrip()
		self._ayudaToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
		self._pictureBox1.BeginInit()
		self._menuStrip1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.AccessibleRole = System.Windows.Forms.AccessibleRole.Sound
		self._button1.BackColor = System.Drawing.Color.LightSkyBlue
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(109, 271)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(107, 36)
		self._button1.TabIndex = 0
		self._button1.Text = "Entrar"
		self._button1.UseCompatibleTextRendering = True
		self._button1.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei UI", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(83, 109)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(163, 34)
		self._label1.TabIndex = 1
		self._label1.Text = "BIENVENIDO"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# usuario
		# 
		self._usuario.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._usuario.Location = System.Drawing.Point(112, 156)
		self._usuario.Name = "usuario"
		self._usuario.Size = System.Drawing.Size(100, 23)
		self._usuario.TabIndex = 2
		self._usuario.Text = "Usuario"
		self._usuario.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(96, 182)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(134, 20)
		self._textBox1.TabIndex = 3
		# 
		# password
		# 
		self._password.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._password.Location = System.Drawing.Point(112, 205)
		self._password.Name = "password"
		self._password.Size = System.Drawing.Size(100, 23)
		self._password.TabIndex = 4
		self._password.Text = "Password"
		self._password.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(96, 231)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(134, 20)
		self._textBox2.TabIndex = 5
		# 
		# pictureBox1
		# 
		self._pictureBox1.Location = System.Drawing.Point(116, 26)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(100, 67)
		self._pictureBox1.TabIndex = 6
		self._pictureBox1.TabStop = False
		# 
		# menuStrip1
		# 
		self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
			[self._ayudaToolStripMenuItem]))
		self._menuStrip1.Location = System.Drawing.Point(0, 0)
		self._menuStrip1.Name = "menuStrip1"
		self._menuStrip1.Size = System.Drawing.Size(316, 24)
		self._menuStrip1.TabIndex = 7
		self._menuStrip1.Text = "menuStrip1"
		# 
		# ayudaToolStripMenuItem
		# 
		self._ayudaToolStripMenuItem.Name = "ayudaToolStripMenuItem"
		self._ayudaToolStripMenuItem.Size = System.Drawing.Size(53, 20)
		self._ayudaToolStripMenuItem.Text = "Ayuda"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.AliceBlue
		self.ClientSize = System.Drawing.Size(316, 357)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._password)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._usuario)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._menuStrip1)
		self.MainMenuStrip = self._menuStrip1
		self.MaximizeBox = False
		self.MinimizeBox = False
		self.Name = "MainForm"
		self.Text = "Login"
		self._pictureBox1.EndInit()
		self._menuStrip1.ResumeLayout(False)
		self._menuStrip1.PerformLayout()
		self.ResumeLayout(False)
		self.PerformLayout()

