using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class B2script : MonoBehaviour
{
    public GameObject u2sticker;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject B1;
    public GameObject B2;
    public GameObject B3;
    public GameObject B4;
    public GameObject B6;
    public GameObject B7;
    public GameObject B8;
    public GameObject B9;
    public GameObject B;
    public GameObject U;
    public GameObject F2;
    public GameObject F;
    public GameObject F8;
    public GameObject D;
    public GameObject M;
    public int correction = 55;
    private int mousedir = 0;
    public int speed;
    private bool pressed = false;
    private bool hasrotated = false;
    Vector3 inicialpos = new Vector3();
    Vector3 finalpos = new Vector3();
    Vector3 deltapos = new Vector3();
    private LayerRotation layerRotation;
    GameObject bchild;
    GameObject dchild;
    GameObject uchild;
    GameObject fchild;

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
            if (B2.transform.childCount > 0)
            {
                Collider collu2 = u2sticker.GetComponentInChildren<Collider>();
                if (collu2.Raycast(ray, out hit, 100.0f))
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
                    // M
                    F2.transform.parent = M.transform;
                    F.transform.parent = M.transform;
                    F8.transform.parent = M.transform;
                    D.transform.parent = M.transform;
                    B8.transform.parent = M.transform;
                    B.transform.parent = M.transform;
                    B2.transform.parent = M.transform;
                    U.transform.parent = M.transform;
                    M.transform.Rotate((speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X")) / 4, 0, 0 * Time.deltaTime);
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
                    // M
                    F2.transform.parent = M.transform;
                    F.transform.parent = M.transform;
                    F8.transform.parent = M.transform;
                    D.transform.parent = M.transform;
                    B8.transform.parent = M.transform;
                    B.transform.parent = M.transform;
                    B2.transform.parent = M.transform;
                    U.transform.parent = M.transform;
                    M.transform.Rotate((speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X")) / 4, 0, 0 * Time.deltaTime);
                    mousedir = 1;
                }
            }
            if (mousedir == 1)
            {
                if (Mathf.Abs(M.transform.rotation.eulerAngles.x) > 268.5 && Mathf.Abs(M.transform.rotation.eulerAngles.x) < 271.5)
                {
                    hasrotated = true;
                    M.transform.rotation = Quaternion.Euler(-90, 0, 0);
                }
                if (Mathf.Abs(M.transform.rotation.eulerAngles.x) > 88.5 && Mathf.Abs(M.transform.rotation.eulerAngles.x) < 91.5)
                {
                    hasrotated = true;
                    M.transform.rotation = Quaternion.Euler(90, 0, 0);
                }
                else
                {
                    M.transform.Rotate(speed * Input.GetAxis("Mouse Y"), 0, 0 * Time.deltaTime);
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
                if (M.transform.rotation.eulerAngles.x > 330)
                {
                    M.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                else
                {
                    if (M.transform.rotation.eulerAngles.x > 265)
                    {
                        M.transform.rotation = Quaternion.Euler(-90, 0, 0);
                        layerRotation.m();
                    }
                    else
                    {
                        if (M.transform.rotation.eulerAngles.x > 30)
                        {
                            M.transform.rotation = Quaternion.Euler(90, 0, 0);
                            layerRotation.mprime();
                        }
                        else
                        {
                            M.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                    }
                }
                F2.transform.parent = Cube2.transform;
                F.transform.parent = Cube2.transform;
                F8.transform.parent = Cube2.transform;
                D.transform.parent = Cube2.transform;
                B8.transform.parent = Cube2.transform;
                B.transform.parent = Cube2.transform;
                B2.transform.parent = Cube2.transform;
                U.transform.parent = Cube2.transform;
                M.transform.rotation = Quaternion.Euler(0, 0, 0);
                uchild = U.transform.GetChild(0).gameObject;
                uchild.transform.parent = null;
                U.transform.rotation = Quaternion.Euler(0, 0, 0);
                U.transform.position = new Vector3(0, 4, 0);
                uchild.transform.parent = U.transform;
                fchild = F.transform.GetChild(0).gameObject;
                fchild.transform.parent = null;
                F.transform.rotation = Quaternion.Euler(0, 0, 0);
                F.transform.position = new Vector3(0, 2, -2);
                fchild.transform.parent = F.transform;
                dchild = D.transform.GetChild(0).gameObject;
                dchild.transform.parent = null;
                D.transform.rotation = Quaternion.Euler(0, 0, 0);
                D.transform.position = new Vector3(0, 0, 0);
                dchild.transform.parent = D.transform;
                bchild = B.transform.GetChild(0).gameObject;
                bchild.transform.parent = null;
                B.transform.rotation = Quaternion.Euler(0, 0, 0);
                B.transform.position = new Vector3(0, 2, 2);
                bchild.transform.parent = B.transform;
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
