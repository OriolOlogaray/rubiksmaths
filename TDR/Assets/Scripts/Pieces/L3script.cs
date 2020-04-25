using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class L3script : MonoBehaviour
{
    public GameObject u7sticker;
    public GameObject f1sticker;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject U1;
    public GameObject U2;
    public GameObject U3;
    public GameObject U4;
    public GameObject U;
    public GameObject U6;
    public GameObject U7;
    public GameObject U8;
    public GameObject U9;
    public GameObject F1;
    public GameObject F2;
    public GameObject F3;
    public GameObject F4;
    public GameObject F;
    public GameObject F6;
    public GameObject F7;
    public GameObject F8;
    public GameObject F9;
    public GameObject L1;
    public GameObject L2;
    public GameObject L3;
    public GameObject L4;
    public GameObject L;
    public GameObject L6;
    public GameObject L7;
    public GameObject L8;
    public GameObject L9;
    public int correction = 55;
    private int sticker = 0;
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
            if (L3.transform.childCount > 0)
            {
                Collider collu7 = u7sticker.GetComponentInChildren<Collider>();
                Collider collf1 = f1sticker.GetComponentInChildren<Collider>();
                if (collu7.Raycast(ray, out hit, 100.0f))
                {
                    sticker = 1;
                    inicialpos = Input.mousePosition;
                    pressed = true;
                }
                if (collf1.Raycast(ray, out hit, 100.0f))
                {
                    sticker = 2;
                    inicialpos = Input.mousePosition;
                    pressed = true;
                }
            }
        }
        if (sticker == 1)
        {
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
                        mousedir = 2;
                    }
                    if (deltapos.y < 0 && deltapos.x > 0)
                    {
                        // F
                        F1.transform.parent = F.transform;
                        F2.transform.parent = F.transform;
                        F3.transform.parent = F.transform;
                        F4.transform.parent = F.transform;
                        F6.transform.parent = F.transform;
                        F7.transform.parent = F.transform;
                        F8.transform.parent = F.transform;
                        F9.transform.parent = F.transform;
                        F.transform.Rotate(0, 0, -speed * correction * Input.GetAxis("Mouse X") * Time.deltaTime);
                        mousedir = 1;
                    }
                    if (deltapos.y > 0 && deltapos.x < 0)
                    {
                        // F
                        F1.transform.parent = F.transform;
                        F2.transform.parent = F.transform;
                        F3.transform.parent = F.transform;
                        F4.transform.parent = F.transform;
                        F6.transform.parent = F.transform;
                        F7.transform.parent = F.transform;
                        F8.transform.parent = F.transform;
                        F9.transform.parent = F.transform;
                        F.transform.Rotate(0, 0, -speed * correction * Input.GetAxis("Mouse X") * Time.deltaTime);
                        mousedir = 1;
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
                        mousedir = 2;
                    }
                }
                if (mousedir == 1)
                {
                    if (Mathf.Abs(F.transform.rotation.eulerAngles.z) > 268.5 && Mathf.Abs(F.transform.rotation.eulerAngles.z) < 271.5)
                    {
                        hasrotated = true;
                        F.transform.rotation = Quaternion.Euler(0, 0, -90);
                    }
                    if (Mathf.Abs(F.transform.rotation.eulerAngles.z) > 88.5 && Mathf.Abs(F.transform.rotation.eulerAngles.z) < 91.5)
                    {
                        hasrotated = true;
                        F.transform.rotation = Quaternion.Euler(0, 0, 90);
                    }
                    else
                    {
                        F.transform.Rotate(0, 0, -speed * correction * Input.GetAxis("Mouse X") * Time.deltaTime);
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
                    if (F.transform.rotation.eulerAngles.z > 330)
                    {
                        F.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (F.transform.rotation.eulerAngles.z > 265)
                        {
                            F.transform.rotation = Quaternion.Euler(0, 0, -90);
                            layerRotation.f();
                        }
                        else
                        {
                            if (F.transform.rotation.eulerAngles.z > 30)
                            {
                                F.transform.rotation = Quaternion.Euler(0, 0, 90);
                                layerRotation.fprime();
                            }
                            else
                            {
                                F.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    F1.transform.parent = Cube2.transform;
                    F2.transform.parent = Cube2.transform;
                    F3.transform.parent = Cube2.transform;
                    F4.transform.parent = Cube2.transform;
                    F6.transform.parent = Cube2.transform;
                    F7.transform.parent = Cube2.transform;
                    F8.transform.parent = Cube2.transform;
                    F9.transform.parent = Cube2.transform;
                    F.transform.rotation = Quaternion.Euler(0, 0, 0);
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
        if (sticker == 2)
        {
            if (pressed == true && !hasrotated)
            {
                if (mousedir == 0)
                {
                    deltapos = Input.mousePosition - inicialpos;
                    if (Mathf.Abs(deltapos.x) > Mathf.Abs(deltapos.y))
                    {
                        // U
                        U1.transform.parent = U.transform;
                        U2.transform.parent = U.transform;
                        U3.transform.parent = U.transform;
                        U4.transform.parent = U.transform;
                        U6.transform.parent = U.transform;
                        U7.transform.parent = U.transform;
                        U8.transform.parent = U.transform;
                        U9.transform.parent = U.transform;
                        U.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
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
                    if (Mathf.Abs(U.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(U.transform.rotation.eulerAngles.y) < 275.5)
                    {
                        hasrotated = true;
                        U.transform.rotation = Quaternion.Euler(0, -90, 0);
                    }
                    if (Mathf.Abs(U.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(U.transform.rotation.eulerAngles.y) < 95.5)
                    {
                        hasrotated = true;
                        U.transform.rotation = Quaternion.Euler(0, 90, 0);
                    }
                    else
                    {
                        U.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
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
                    if (U.transform.rotation.eulerAngles.y > 330)
                    {
                        U.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (U.transform.rotation.eulerAngles.y > 265)
                        {
                            U.transform.rotation = Quaternion.Euler(0, -90, 0);
                            layerRotation.uprime();
                        }
                        else
                        {
                            if (U.transform.rotation.eulerAngles.y > 30)
                            {
                                U.transform.rotation = Quaternion.Euler(0, 90, 0);
                                layerRotation.u();
                            }
                            else
                            {
                                U.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    U1.transform.parent = Cube2.transform;
                    U2.transform.parent = Cube2.transform;
                    U3.transform.parent = Cube2.transform;
                    U4.transform.parent = Cube2.transform;
                    U6.transform.parent = Cube2.transform;
                    U7.transform.parent = Cube2.transform;
                    U8.transform.parent = Cube2.transform;
                    U9.transform.parent = Cube2.transform;
                    U.transform.rotation = Quaternion.Euler(0, 0, 0);
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
}
