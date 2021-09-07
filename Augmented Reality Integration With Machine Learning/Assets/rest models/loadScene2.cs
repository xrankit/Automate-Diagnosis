using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class loadScene2 : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }
    public void  play_game()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 2);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
