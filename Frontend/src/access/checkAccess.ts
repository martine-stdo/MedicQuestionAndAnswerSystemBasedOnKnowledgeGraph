/**
 * 检查权限
 * @param loginUser 当前登录用户
 * @param needAccess 需要的权限
 * @returns boolean 有无权限
 */

import { ACCESS_ENUM } from "./accessEnum";

const checkAccess = (loginUser: any, needAccess = ACCESS_ENUM.NOT_LOGIN) => {
  //获取当前登录用户的权限(如果没有loginUser,则表示未登录)
  const loginUserAccess = loginUser?.userRole ?? ACCESS_ENUM.NOT_LOGIN;
  //用户未登录也能查看
  if (needAccess === ACCESS_ENUM.NOT_LOGIN) {
    return true;
  }

  //用户登录才能查看
  if (needAccess === ACCESS_ENUM.USER) {
    if (loginUserAccess === ACCESS_ENUM.NOT_LOGIN) {
      return false;
    }
  }

  //如果需要管理员权限才能查看

  if (needAccess === ACCESS_ENUM.ADMIN) {
    if (loginUserAccess !== ACCESS_ENUM.ADMIN) {
      return false;
    }
  }

  return true;
};

export default checkAccess;
