using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class L2script : MonoBehaviour
{
    public GameObject u4sticker;
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
    public GameObject U;
    public GameObject R;
    public GameObject R2;
    public GameObject R8;
    public GameObject D;
    public GameObject S;
    public int correction = 55;
    private int mousedir = 0;
    public int speed;
    private bool pressed = false;
    private bool hasrotated = false;
    Vector3 inicialpos = new Vector3();
    Vector3 finalpos = new Vector3();
    Vector3 deltapos = new Vector3();
    private LayerRotation layerRotation;
    GameObject uchild;
    GameObject rchild;
    GameObject dchild;
    GameObject lchild;

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
            if (L2.transform.childCount > 0)
            {
                Collider collu4 = u4sticker.GetComponentInChildren<Collider>();
                if (collu4.Raycast(ray, out hit, 100.0f))
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
                    // S
                    L2.transform.parent = S.transform;
                    U.transform.parent = S.transform;
                    R2.transform.parent = S.transform;
                    R.transform.parent = S.transform;
                    R8.transform.parent = S.transform;
                    D.transform.parent = S.transform;
                    L8.transform.parent = S.transform;
                    L.transform.parent = S.transform;
                    S.transform.Rotate(0, 0, (speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X")) * correction / 4 * Time.deltaTime);
                    mousedir = 2;
                }
                if (deltapos.y > 0 && deltapos.x < 0)
                {
                    // S
                    L2.transform.parent = S.transform;
                    U.transform.parent = S.transform;
                    R2.transform.parent = S.transform;
                    R.transform.parent = S.transform;
                    R8.transform.parent = S.transform;
                    D.transform.parent = S.transform;
                    L8.transform.parent = S.transform;
                    L.transform.parent = S.transform;
                    S.transform.Rotate(0, 0, (speed * Input.GetAxis("Mouse Y") * Input.GetAxis("Mouse X")) * correction / 4 * Time.deltaTime);
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
                if (Mathf.Abs(S.transform.rotation.eulerAngles.z) > 268.5 && Mathf.Abs(S.transform.rotation.eulerAngles.z) < 271.5)
                {
                    hasrotated = true;
                    S.transform.rotation = Quaternion.Euler(0, 0, -90);
                }
                if (Mathf.Abs(S.transform.rotation.eulerAngles.z) > 88.5 && Mathf.Abs(S.transform.rotation.eulerAngles.z) < 91.5)
                {
                    hasrotated = true;
                    S.transform.rotation = Quaternion.Euler(0, 0, 90);
                }
                else
                {
                    S.transform.Rotate(0, 0, speed * correction * Input.GetAxis("Mouse Y") * Time.deltaTime);
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
                if (S.transform.rotation.eulerAngles.z > 330)
                {
                    S.transform.rotation = Quaternion.Euler(0, 0, 0);
                }
                else
                {
                    if (S.transform.rotation.eulerAngles.z > 265)
                    {
                        S.transform.rotation = Quaternion.Euler(0, 0, -90);
                        layerRotation.s();
                    }
                    else
                    {
                        if (S.transform.rotation.eulerAngles.z > 30)
                        {
                            S.transform.rotation = Quaternion.Euler(0, 0, 90);
                            layerRotation.sprime();
                        }
                        else
                        {
                            S.transform.rotation = Quaternion.Euler(0, 0, 0);
                        }
                    }
                }
                L2.transform.parent = Cube2.transform;
                U.transform.parent = Cube2.transform;
                R2.transform.parent = Cube2.transform;
                R.transform.parent = Cube2.transform;
                R8.transform.parent = Cube2.transform;
                D.transform.parent = Cube2.transform;
                L8.transform.parent = Cube2.transform;
                L.transform.parent = Cube2.transform;
                S.transform.rotation = Quaternion.Euler(0, 0, 0);
                uchild = U.transform.GetChild(0).gameObject;
                uchild.transform.parent = null;
                U.transform.rotation = Quaternion.Euler(0, 0, 0);
                U.transform.position = new Vector3(0, 4, 0);
                uchild.transform.parent = U.transform;
                lchild = L.transform.GetChild(0).gameObject;
                lchild.transform.parent = null;
                L.transform.rotation = Quaternion.Euler(0, 0, 0);
                L.transform.position = new Vector3(-2, 2, 0);
                lchild.transform.parent = L.transform;
                dchild = D.transform.GetChild(0).gameObject;
                dchild.transform.parent = null;
                D.transform.rotation = Quaternion.Euler(0, 0, 0);
                D.transform.position = new Vector3(0, 0, 0);
                dchild.transform.parent = D.transform;
                rchild = R.transform.GetChild(0).gameObject;
                rchild.transform.parent = null;
                R.transform.rotation = Quaternion.Euler(0, 0, 0);
                R.transform.position = new Vector3(2, 2, 0);
                rchild.transform.parent = R.transform;
            }
            hasrotated = false;
            mousedir = 0;
            pressed = false;
        }
    }
}
