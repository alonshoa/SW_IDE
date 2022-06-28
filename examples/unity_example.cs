using UnityEngine;
using UnityEditor;

public class ScriptBuilder:EditorWindow
{
	OpenAI openai = new OpenAI();
	string instruction;
	string code;

	[MenuItem("Window/ScriptBuilder")]
	public static void ShowWindow()
	{
		GetWindow<ScriptBuilder>("ScriptBuilder");
	}

	void OnGUI()
	{
		instruction = EditorGUILayout.TextArea(instruction,GUILayout.Height(100));
		code = EditorGUILayout.TextArea(code,GUILayout.Height(100));
		if(GUILayout.Button("Send to OpenAI"))
		{
			OpenAIResult result = openai.sendToOpenAI(instruction,code);
			Debug.Log(result.code);
		}
	}
}



