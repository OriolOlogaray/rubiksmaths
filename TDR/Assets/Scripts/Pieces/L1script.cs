using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class L1script : MonoBehaviour
{
    public GameObject u1sticker;
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
    public GameObject B1;
    public GameObject B2;
    public GameObject B3;
    public GameObject B4;
    public GameObject B6;
    public GameObject B7;
    public GameObject B8;
    public GameObject B9;
    public GameObject B;
    public int correction = 55;
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
            if (L1.transform.childCount > 0)
            {
                Collider collu1 = u1sticker.GetComponentInChildren<Collider>();
                if (collu1.Raycast(ray, out hit, 100.0f))
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
                if (deltapos.y > 0 && deltapos.x > 0)
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
                    L.transform.Rotate((speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X")) / 4, 0, 0 * Time.deltaTime);
                    mousedir = 1;
                }
                if (deltapos.y < 0 && deltapos.x > 0)
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
                    B.transform.Rotate(0, 0, (speed * Input.GetAxis("Mouse Y") * correction * Input.GetAxis("Mouse X")) / 4 * Time.deltaTime);
                    mousedir = 2;
                }
                if (deltapos.y > 0 && deltapos.x < 0)
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
                    B.transform.Rotate(0, 0, (speed * Input.GetAxis("Mouse Y") * correction * Input.GetAxis("Mouse X")) / 4 * Time.deltaTime);
                    mousedir = 2;
                }
                if (deltapos.y < 0 && deltapos.x < 0)
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
                    L.transform.Rotate((speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X")) / 4, 0, 0 * Time.deltaTime);
                    mousedir = 1;
                }               
            }
            if (mousedir == 1)
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
