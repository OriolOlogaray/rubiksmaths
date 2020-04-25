using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class R6script : MonoBehaviour
{
    public GameObject r6sticker;
    public GameObject Cube;
    public GameObject Cube2;
    public GameObject B1;
    public GameObject B2;
    public GameObject B3;
    public GameObject B4;
    public GameObject B;
    public GameObject B6;
    public GameObject B7;
    public GameObject B8;
    public GameObject B9;
    public GameObject L;
    public GameObject L4;
    public GameObject L6;
    public GameObject R;
    public GameObject R4;
    public GameObject R6;
    public GameObject F;
    public GameObject E;
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
    GameObject fchild;
    GameObject lchild;
    GameObject bchild;
    GameObject rchild;

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
            if (R6.transform.childCount > 0)
            {
                Collider collr6 = r6sticker.GetComponentInChildren<Collider>();
                if (collr6.Raycast(ray, out hit, 100.0f))
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
                    // E
                    R6.transform.parent = E.transform;
                    R.transform.parent = E.transform;
                    R4.transform.parent = E.transform;
                    F.transform.parent = E.transform;
                    L6.transform.parent = E.transform;
                    L.transform.parent = E.transform;
                    L4.transform.parent = E.transform;
                    B.transform.parent = E.transform;
                    E.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
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
                if (Mathf.Abs(E.transform.rotation.eulerAngles.y) > 268.5 && Mathf.Abs(E.transform.rotation.eulerAngles.y) < 275.5)
                {
                    hasrotated = true;
                    E.transform.rotation = Quaternion.Euler(0, -90, 0);
                }
                if (Mathf.Abs(E.transform.rotation.eulerAngles.y) > 88.5 && Mathf.Abs(E.transform.rotation.eulerAngles.y) < 95.5)
                {
                    hasrotated = true;
                    E.transform.rotation = Quaternion.Euler(0, 90, 0);
                }
                else
                {
                    E.transform.Rotate(0, -speed * Input.GetAxis("Mouse X"), 0 * Time.deltaTime);
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
                if (E.transform.rotation.eulerAngles.y > 330)
                {
                    E.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                else
                {
                    if (E.transform.rotation.eulerAngles.y > 265)
                    {
                        E.transform.rotation = Quaternion.Euler(0, -90, 0);
                        layerRotation.e();
                    }
                    else
                    {
                        if (E.transform.rotation.eulerAngles.y > 30)
                        {
                            E.transform.rotation = Quaternion.Euler(0, 90, 0);
                            layerRotation.eprime();
                        }
                        else
                        {
                            E.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                    }
                }
                R6.transform.parent = Cube2.transform;
                R.transform.parent = Cube2.transform;
                R4.transform.parent = Cube2.transform;
                F.transform.parent = Cube2.transform;
                L6.transform.parent = Cube2.transform;
                L.transform.parent = Cube2.transform;
                L4.transform.parent = Cube2.transform;
                B.transform.parent = Cube2.transform;
                E.transform.rotation = Quaternion.Euler(0, 0, 0);
                rchild = R.transform.GetChild(0).gameObject;
                rchild.transform.parent = null;
                R.transform.rotation = Quaternion.Euler(0, 0, 0);
                R.transform.position = new Vector3(2, 2, 0);
                rchild.transform.parent = R.transform;
                fchild = F.transform.GetChild(0).gameObject;
                fchild.transform.parent = null;
                F.transform.rotation = Quaternion.Euler(0, 0, 0);
                F.transform.position = new Vector3(0, 2, -2);
                fchild.transform.parent = F.transform;
                lchild = L.transform.GetChild(0).gameObject;
                lchild.transform.parent = null;
                L.transform.rotation = Quaternion.Euler(0, 0, 0);
                L.transform.position = new Vector3(-2, 2, 0);
                lchild.transform.parent = L.transform;
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
