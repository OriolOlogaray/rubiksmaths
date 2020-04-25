using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class L9script : MonoBehaviour
{
    public GameObject f7sticker;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject L1;
    public GameObject L2;
    public GameObject L3;
    public GameObject L4;
    public GameObject L;
    public GameObject L6;
    public GameObject L7;
    public GameObject L8;
    public GameObject L9;
    public GameObject R7;
    public GameObject R8;
    public GameObject R9;
    public GameObject F8;
    public GameObject B8;
    public GameObject D;
    private int mousedir = 0;
    public int speed;
    private bool pressed = false;
    private bool hasrotated = false;
    Vector3 inicialpos = new Vector3();
    Vector3 finalpos = new Vector3();
    Vector3 deltapos = new Vector3();
    private LayerRotation layerRotation;
    void Awake()
    {
        layerRotation = Cube.GetComponent<LayerRotation>();
    }
    void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit hit;
            if (L9.transform.childCount > 0)
            {
                Collider collf7 = f7sticker.GetComponentInChildren<Collider>();
                if (collf7.Raycast(ray, out hit, 100.0f))
                {
                    inicialpos = Input.mousePosition;
                    pressed = true;
                }
            }
        }
        if (pressed == true && !hasrotated)
        {
            if (mousedir == 0)
            {
                deltapos = Input.mousePosition - inicialpos;
                if (Mathf.Abs(deltapos.x) > Mathf.Abs(deltapos.y))
                {
                    // D
                    L9.transform.parent = D.transform;
                    F8.transform.parent = D.transform;
                    R7.transform.parent = D.transform;
                    R8.transform.parent = D.transform;
                    R9.transform.parent = D.transform;
                    B8.transform.parent = D.transform;
                    L7.transform.parent = D.transform;
                    L8.transform.parent = D.transform;
                    D.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
                    mousedir = 1;
                }
                if (Mathf.Abs(deltapos.x) < Mathf.Abs(deltapos.y))
                {
                    // L
                    L1.transform.parent = L.transform;
                    L2.transform.parent = L.transform;
                    L3.transform.parent = L.transform;
                    L4.transform.parent = L.transform;
                    L6.transform.parent = L.transform;
                    L7.transform.parent = L.transform;
                    L8.transform.parent = L.transform;
                    L9.transform.parent = L.transform;
                    L.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
                    mousedir = 2;
                }
            }
            if (mousedir == 1)
            {
                if (Mathf.Abs(D.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(D.transform.rotation.eulerAngles.y) < 275.5)
                {
                    hasrotated = true;
                    D.transform.rotation = Quaternion.Euler(0, -90, 0);
                }
                if (Mathf.Abs(D.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(D.transform.rotation.eulerAngles.y) < 95.5)
                {
                    hasrotated = true;
                    D.transform.rotation = Quaternion.Euler(0, 90, 0);
                }
                else
                {
                    D.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
                }
            }
            if (mousedir == 2)
            {
                if (Mathf.Abs(L.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(L.transform.rotation.eulerAngles.x) < 271.5)
                {
                    hasrotated = true;
                    L.transform.rotation = Quaternion.Euler(-90, 0, 0);
                }
                if (Mathf.Abs(L.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(L.transform.rotation.eulerAngles.x) < 91.5)
                {
                    hasrotated = true;
                    L.transform.rotation = Quaternion.Euler(90, 0, 0);
                }
                else
                {
                    L.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
                }
            }
        }
        if (Input.GetMouseButtonUp(0))
        {
            finalpos = Input.mousePosition;
            deltapos = finalpos - inicialpos;
            if (mousedir == 1)
            {
                if (D.transform.rotation.eulerAngles.y > 330)
                {
                    D.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                else
                {
                    if (D.transform.rotation.eulerAngles.y > 265)
                    {
                        D.transform.rotation = Quaternion.Euler(0, -90, 0);
                        layerRotation.d();
                    }
                    else
                    {
                        if (D.transform.rotation.eulerAngles.y > 30)
                        {
                            D.transform.rotation = Quaternion.Euler(0, 90, 0);
                            layerRotation.dprime();
                        }
                        else
                        {
                            D.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                    }
                }
                L9.transform.parent = Cube2.transform;
                F8.transform.parent = Cube2.transform;
                R7.transform.parent = Cube2.transform;
                R8.transform.parent = Cube2.transform;
                R9.transform.parent = Cube2.transform;
                B8.transform.parent = Cube2.transform;
                L7.transform.parent = Cube2.transform;
                L8.transform.parent = Cube2.transform;
                D.transform.rotation = Quaternion.Euler(0, 0, 0);
            }
            if (mousedir == 2)
            {
                if (L.transform.rotation.eulerAngles.x > 330)
                {
                    L.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                else
                {
                    if (L.transform.rotation.eulerAngles.x > 265)
                    {
                        L.transform.rotation = Quaternion.Euler(-90, 0, 0);
                        layerRotation.l();
                    }
                    else
                    {
                        if (L.transform.rotation.eulerAngles.x > 30)
                        {
                            L.transform.rotation = Quaternion.Euler(90, 0, 0);
                            layerRotation.lprime();
                        }
                        else
                        {
                            L.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                    }
                }
                L1.transform.parent = Cube2.transform;
                L2.transform.parent = Cube2.transform;
                L3.transform.parent = Cube2.transform;
                L4.transform.parent = Cube2.transform;
                L6.transform.parent = Cube2.transform;
                L7.transform.parent = Cube2.transform;
                L8.transform.parent = Cube2.transform;
                L9.transform.parent = Cube2.transform;
                L.transform.rotation = Quaternion.Euler(0, 0, 0);
            }
            hasrotated = false;
            mousedir = 0;
            pressed = false;
        }
    }
}
