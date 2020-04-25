using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class R9script : MonoBehaviour
{
    public GameObject r9sticker;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject B1;
    public GameObject B2;
    public GameObject B3;
    public GameObject B4;
    public GameObject B;
    public GameObject B6;
    public GameObject B7;
    public GameObject B9;
    public GameObject L7;
    public GameObject L8;
    public GameObject L9;
    public GameObject R7;
    public GameObject R8;
    public GameObject R9;
    public GameObject F8;
    public GameObject B8;
    public GameObject D;
    public int correction = 50;
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
            if (R9.transform.childCount > 0)
            {
                Collider collr9 = r9sticker.GetComponentInChildren<Collider>();
                if (collr9.Raycast(ray, out hit, 100.0f))
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
                    // B
                    B1.transform.parent = B.transform;
                    B2.transform.parent = B.transform;
                    B3.transform.parent = B.transform;
                    B4.transform.parent = B.transform;
                    B6.transform.parent = B.transform;
                    B7.transform.parent = B.transform;
                    B8.transform.parent = B.transform;
                    B9.transform.parent = B.transform;
                    B.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
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
                if (Mathf.Abs(B.transform.rotation.eulerAngles.z) > 268.5 && Mathf.Abs(B.transform.rotation.eulerAngles.z) < 271.5)
                {
                    hasrotated = true;
                    B.transform.rotation = Quaternion.Euler(0, 0, -90);
                }
                if (Mathf.Abs(B.transform.rotation.eulerAngles.z) > 88.5 && Mathf.Abs(B.transform.rotation.eulerAngles.z) < 91.5)
                {
                    hasrotated = true;
                    B.transform.rotation = Quaternion.Euler(0, 0, 90);
                }
                else
                {
                    B.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
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
                if (B.transform.rotation.eulerAngles.z > 330)
                {
                    B.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                else
                {
                    if (B.transform.rotation.eulerAngles.z > 265)
                    {
                        B.transform.rotation = Quaternion.Euler(0, 0, -90);
                        layerRotation.bprime();
                    }
                    else
                    {
                        if (B.transform.rotation.eulerAngles.z > 30)
                        {
                            B.transform.rotation = Quaternion.Euler(0, 0, 90);
                            layerRotation.b();
                        }
                        else
                        {
                            B.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                    }
                }
                B1.transform.parent = Cube2.transform;
                B2.transform.parent = Cube2.transform;
                B3.transform.parent = Cube2.transform;
                B4.transform.parent = Cube2.transform;
                B6.transform.parent = Cube2.transform;
                B7.transform.parent = Cube2.transform;
                B8.transform.parent = Cube2.transform;
                B9.transform.parent = Cube2.transform;
                B.transform.rotation = Quaternion.Euler(0, 0, 0);
            }
            hasrotated = false;
            mousedir = 0;
            pressed = false;
        }
    }
}
