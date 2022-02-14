extends Node2D


onready var animation = $AnimationPlayer
onready var label = $Label


var charadas = [
	"""Tem raízes misteriosas
	É mais alta que as frondosa
	Sobe, sobe e tambem desce,
	Mas não cresce nem decresce.""",
	"""
	Trinta cavalos brancos na colina avermelhada
	Primeiro cerceiam,
	Depois pisoteiam,
	Depois nao fazem nada.
	""",
	
	
]


func _physics_process(delta):
	pass

func _ready():
	randomize()

func _on_Button_pressed():
	animation.play("fade")
	$Timer.start()

func _on_Timer_timeout():
	animation.play("fade")
	
func change_text():
	var random = randi()%2
	label.text = charadas[random]


	
