using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class R3script : MonoBehaviour
{
    public GameObject u3sticker;
    public GameObject r3sticker;
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
    public GameObject R1;
    public GameObject R2;
    public GameObject R3;
    public GameObject R4;
    public GameObject R;
    public GameObject R6;
    public GameObject R7;
    public GameObject R8;
    public GameObject R9;
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
            if (R3.transform.childCount > 0)
            {
                Collider collu3 = u3sticker.GetComponentInChildren<Collider>();
                Collider collr3 = r3sticker.GetComponentInChildren<Collider>();
                if (collu3.Raycast(ray, out hit, 100.0f))
                {
                    sticker = 1;
                    inicialpos = Input.mousePosition;
                    pressed = true;
                }
                if (collr3.Raycast(ray, out hit, 100.0f))
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
                        //R
                        R1.transform.parent = R.transform;
                        R2.transform.parent = R.transform;
                        R3.transform.parent = R.transform;
                        R4.transform.parent = R.transform;
                        R6.transform.parent = R.transform;
                        R7.transform.parent = R.transform;
                        R8.transform.parent = R.transform;
                        R9.transform.parent = R.transform;
                        R.transform.Rotate(speed * Input.GetAxis("Mouse X"), 0, 0 * Time.deltaTime);
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
                        //R
                        R1.transform.parent = R.transform;
                        R2.transform.parent = R.transform;
                        R3.transform.parent = R.transform;
                        R4.transform.parent = R.transform;
                        R6.transform.parent = R.transform;
                        R7.transform.parent = R.transform;
                        R8.transform.parent = R.transform;
                        R9.transform.parent = R.transform;
                        R.transform.Rotate(speed * Input.GetAxis("Mouse X"), 0, 0 * Time.deltaTime);
                        mousedir = 1;
                    }
                }
                if (mousedir == 1)
                {
                    if (Mathf.Abs(R.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(R.transform.rotation.eulerAngles.x) < 271.5)
                    {
                        hasrotated = true;
                        R.transform.rotation = Quaternion.Euler(-90, 0, 0);
                    }
                    if (Mathf.Abs(R.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(R.transform.rotation.eulerAngles.x) < 91.5)
                    {
                        hasrotated = true;
                        R.transform.rotation = Quaternion.Euler(90, 0, 0);
                    }
                    else
                    {
                        R.transform.Rotate(speed * Input.GetAxis("Mouse X"), 0, 0 * Time.deltaTime);
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
                    if (R.transform.rotation.eulerAngles.x > 330)
                    {
                        R.transform.rotation = Quaternion.Euler(0, 0, 0);
                    }
                    else
                    {
                        if (R.transform.rotation.eulerAngles.x > 265)
                        {
                            R.transform.rotation = Quaternion.Euler(-90, 0, 0);
                            layerRotation.rprime();
                        }
                        else
                        {
                            if (R.transform.rotation.eulerAngles.x > 30)
                            {
                                R.transform.rotation = Quaternion.Euler(90, 0, 0);
                                layerRotation.r();
                            }
                            else
                            {
                                R.transform.rotation = Quaternion.Euler(0, 0, 0);
                            }
                        }
                    }
                    R1.transform.parent = Cube2.transform;
                    R2.transform.parent = Cube2.transform;
                    R3.transform.parent = Cube2.transform;
                    R4.transform.parent = Cube2.transform;
                    R6.transform.parent = Cube2.transform;
                    R7.transform.parent = Cube2.transform;
                    R8.transform.parent = Cube2.transform;
                    R9.transform.parent = Cube2.transform;
                    R.transform.rotation = Quaternion.Euler(0, 0, 0);
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
}
